__author__ = 'yenda'

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple


class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return {"image": obj.image_url(), "name": obj.get_full_name()}


class ReportForm(forms.Form):
    error_messages = {
        'unexpected_students': "Some of the reported students should not be in this class.",
    }

    students = MyModelMultipleChoiceField(settings.AUTH_USER_MODEL,
                                          widget=CheckboxSelectMultiple,
                                          required=False
                                          )

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop("event")
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['students'].queryset = get_user_model().objects.filter(memberships__in=self.event.memberships.all())

    def clean_students(self):
        """ Validate that the pension takes pet.species """
        students_pk = self.cleaned_data.get('students')
        if not students_pk:
            return []
        students = get_user_model().objects.filter(memberships__in=self.event.memberships.all(), pk__in=students_pk)
        if not students:
            raise forms.ValidationError(self.error_messages['unexpected_students'])
        return students
