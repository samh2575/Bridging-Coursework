from django.test import *
from django.urls import resolve
from django.http import HttpRequest
from django.urls import *

from cv.models import cv as cv_model
from django.contrib.auth.models import User
from django.utils import timezone
import time

class Test_Database(TestCase):
    
    me = User.objects.get(username='sam')

    def test_cv(self, me=me):
        test_entry = cv_model.objects.create(about="test", work="test2", education='test3', author=me, updated=timezone.now())
        time.sleep(1)
        self.assertEqual(test_entry.about, 'test')
        self.assertEqual(test_entry.work, 'test2')
        self.assertEqual(test_entry.education, 'test3')
        self.assertEqual(test_entry.author, me)


class cvPageTests(TestCase):

    def test_cv_page_status_code(self):
        response = self.client.get('/cv/')
        self.assertEquals(response.status_code, 200)
    
    def test_cv_edit_status_code(self):
        response = self.client.get('/cv/edit/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('cv'))
        self.assertEquals(response.status_code, 200)

    def test_edit_view_url_by_name(self):
        response = self.client.get(reverse('cv_edit'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cv'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv/cv.html', 'cv/base.html')

    def test_edit_view_uses_correct_template(self):
        response = self.client.get(reverse('cv_edit'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv/cv_edit.html', 'cv/base.html')

    def test_cv_page_contains_correct_html(self):
        response = self.client.get('/cv/')
        self.assertContains(response, 'Curriculum Vitae')

    def test_cv_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/cv/')
        self.assertNotContains(
            response, 'Technology Degree Apprentice at PwC, studying Computer Science at the University of Birmingham')

