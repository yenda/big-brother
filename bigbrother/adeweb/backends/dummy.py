__author__ = 'yenda'

import os

from .api import GenericApi


class API(GenericApi):
    def get_activities(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../activities.xml')
        with open(path, "r") as f:
            resources = f.read()
            return resources

    def get_resources(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources.xml')
        with open(path, "r") as f:
            resources = f.read()
            return resources