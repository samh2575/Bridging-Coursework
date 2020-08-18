from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.urls import reverse

from blog.models import Post as blog_model
from django.contrib.auth.models import User
from django.utils import timezone
import time


class BlogPageTests(TestCase):

    def test_blog_page_status_code(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)

    def test_new_view_url_by_name(self):
        response = self.client.get(reverse('post_new'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html', 'blog/base.html')

    def test_new_view_uses_correct_template(self):
        response = self.client.get(reverse('post_new'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html', 'blog/base.html')

    def test_blog_new_contains_correct_html(self):
        response = self.client.get('/blog/post/new/')
        self.assertContains(response, 'Blog') ## change ##

    def test_blog_page_contains_correct_html(self):
        response = self.client.get('/blog/')
        self.assertContains(response, 'Blog') ## change ##

    def test_blog_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/blog/')
        self.assertNotContains(response, 'Technology Degree Apprentice at PwC, studying Computer Science at the University of Birmingham')
    
    def test_blog_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/blog/post/new/')
        self.assertNotContains(response, 'published')


