__author__ = 'yenda'
from django.db import models
from django.contrib.auth.models import AbstractUser
from djchoices import DjangoChoices, ChoiceItem
from django.utils.translation import ugettext_lazy as _


class Category(DjangoChoices):
    student = ChoiceItem('student', label=_('student'))
    instructor = ChoiceItem('instructor', label=_('instructor'))


class User(AbstractUser):
    adeweb_id = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.student)

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.username

    def is_instructor(self):
        return self.category=="instructor"