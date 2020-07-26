from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.urls import reverse

class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html', 'home/base.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        # self.assertContains(response, '<h1>Sam Harrison</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')