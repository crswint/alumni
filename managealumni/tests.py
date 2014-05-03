"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import WelcomeView, AlumniList, LookingForWorkView


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class UrlTests(TestCase):
    def test_welcome_url(self):
        """Tests when we go to the welcome url it loads the welcome view"""
        welcome = resolve(reverse('managealumni:welcome'))
        return self.assertEqual(welcome.func.__name__,
                                WelcomeView.__name__)

    def test_alumnilist_url(self):
        """Tests when we go to the alumnilist url loads the alumnilist view"""
        alumnilist = resolve(reverse('managealumni:alumnilist'))
        return self.assertEqual(alumnilist.func.__name__,
                                AlumniList.__name__)

    def test_lfw_url(self):
        """Tests when we go to the lfw url it loads the lookingforwork view"""
        lfw = resolve(reverse('managealumni:lfw'))
        return self.assertEqual(lfw.func.__name__,
                                LookingForWorkView.__name__)