__author__ = 'yenda'

from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(required=True)