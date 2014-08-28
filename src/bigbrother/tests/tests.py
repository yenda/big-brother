__author__ = 'yenda'
from decimal import Decimal
import json

from django.conf import settings
from django.http import HttpRequest, QueryDict
from django.test import TestCase
from django.utils.importlib import import_module

from rest_framework.request import Request
from mock import patch, MagicMock

from hdov.pensions.tests.factory_models import PensionFactory
from hdov.utils.googlemaps import geolocation, get_pension_distance


class GoogleMapsTests(TestCase):
    def test_geolocation_valid_address(self):
        lat, lng = geolocation('Herengracht 416, Amsterdam, The Netherlands')

        self.assertAlmostEqual(lat, Decimal('52.367'), delta=Decimal('0.01'))
        self.assertAlmostEqual(lng, Decimal('4.887'), delta=Decimal('0.01'))


class GoogleDistanceTests(TestCase):
    def setUp(self):
        # create a request with a querystring and a session
        # geocoordinates of 'Amsterdam'
        self.lat = '52.3702157'
        self.lng = '4.895167900000001'
        qs = 'lat={0}&lng={1}'.format(self.lat, self.lng)

        # Distance Amsterdam - Rotterdam by car ~ 75.7 km

        request = HttpRequest()
        request.GET = QueryDict(qs)
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore(None)
        # rest_framework request
        self.request = Request(request)

        self.pension = PensionFactory(latitude=Decimal('51.918862'), longitude=Decimal('4.474075')) # Rotterdam

        # stripped down response data (bare minimum)
        self.response_data = {
            'status': 'OK',
            'rows': [{
                'elements': [{
                    'status': 'OK',
                    'distance': {
                        'value': 76940,
                        'text': '77 km',
                    }
                }]
            }]
        }

    def test_distance(self):
        """ Test that the driving distance is returned from `get_pension_distance` """

        # Real API call
        distance = get_pension_distance(self.pension, self.request)
        self.assertAlmostEqual(distance, 76.0, delta=1.0)

    @patch('requests.get')
    def test_session_distance_cache(self, mock):
        SESSION_KEY = 'cached_distances'

        response = MagicMock()
        response.content = json.dumps(self.response_data)
        response.status_code = 200
        mock.return_value = response

        distance = get_pension_distance(self.pension, self.request)
        self.assertAlmostEqual(distance, 76.0, delta=1.0)

        # test session
        self.assertIn(SESSION_KEY, self.request.session)
        cache_dict = self.request.session[SESSION_KEY]

        # location tuple as key for the location
        location_key = (
            "{:.4f}".format(float(self.lat)),
            "{:.4f}".format(float(self.lng))
        )

        location_cache = cache_dict.get(location_key)
        self.assertIsNotNone(location_cache)
        # make sure that only one requests.get call was done
        self.assertEqual(mock.call_count, 1)

        # test that the distance is correctly stored
        self.assertEqual(distance, location_cache.get(self.pension.pk))

        # get the distance again, this time from cache
        get_pension_distance(self.pension, self.request)
        self.assertEqual(mock.call_count, 1) # > 1 ==> not from cache

    @patch('requests.get')
    def test_fallback_wrong_status_code(self, mock):
        response = MagicMock()
        response.content = 'NotFound'
        response.status_code = 404
        mock.return_value = response

        distance = get_pension_distance(self.pension, self.request)
        # straight line distance ~ 69 km
        self.assertAlmostEqual(distance, 69.0, delta=5.0)

    @patch('requests.get')
    def test_fallback_over_query_limit(self, mock):
        response = MagicMock()
        response.content = json.dumps({'status': 'OVER_QUERY_LIMIT'})
        response.status_code = 200
        mock.return_value = response

        distance = get_pension_distance(self.pension, self.request)
        # straight line distance ~ 69 km
        self.assertAlmostEqual(distance, 69.0, delta=5.0)