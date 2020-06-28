from django.urls import resolve
from django.test import TestCase
from blog.views import post_list
from django.http import HttpRequest
from django.http import HttpResponse
from django.test import Client
# Create your tests here.

# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')  
    #     self.assertEqual(found.func, post_list)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html', 'blog/base.html')

    # def test_home_page_returns_correct_html(self):

    #     response = self.client.get('/')
    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn("<title>Sam's Blog</title>", html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     ​self.assertTemplateUsed(response, 'post_list.html')

        # #We create a HttpRequest object, which is what Django will see when a user’s browser asks for a page.
        # request = HttpRequest()
        # #We pass it to our home_page view, which gives us a response. You won’t be surprised to hear that this object is an instance of a class called HttpResponse.
        # response = post_list(request)
        # #Then, we extract the .content of the response. These are the raw bytes, the ones and zeros that would be sent down the wire to the user’s browser. We call .decode() to convert them into the string of HTML that’s being sent to the user.
        # html = response.content.decode('utf8')
        # #We want it to start with an <html> tag which gets closed at the end*.
        # self.assertTrue(html.strip().startswith('<html>'))#'<div class="post">'))
        # #And we want a <title> tag somewhere in the middle, with the words "Sams Blog" in it—​because that’s what we specified in our functional test.
        # self.assertIn("<title>Sam's Blog</title>", html)
        # #*closed at the end
        # self.assertTrue(html.strip().endswith('</html>'))#'</div>'))