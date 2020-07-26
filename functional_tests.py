from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_makenedit_a_cv_and_retrieve_it_later(self):
    
        self.browser.get('http://127.0.0.1:8000/admin/')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('sam')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('password')
        password.send_keys(Keys.ENTER)

        time.sleep(2)

        self.browser.get('http://127.0.0.1:8000/cv/edit/')
        
        self.assertIn('Sam Harrison', self.browser.title)

        about = self.browser.find_element_by_id('id_about')
        about.send_keys('my name is sam')
        work = self.browser.find_element_by_id('id_work')
        work.send_keys('PwC')
        skills = self.browser.find_element_by_id('id_skills')
        skills.send_keys('i have skills')
        education = self.browser.find_element_by_id('id_education')
        education.send_keys('UoB')

        button = self.browser.find_element_by_id('submitbtn')
        button.click()

        time.sleep(2)

        aboutnew = self.browser.find_element_by_id('about')
        self.assertTrue('my name is sam', aboutnew)

        worknew = self.browser.find_element_by_id('work')
        self.assertTrue('PwC', worknew)

        skillsnew = self.browser.find_element_by_id('skills')
        self.assertTrue('i have skills', worknew)

        edunew = self.browser.find_element_by_id('edu')
        self.assertTrue('UoB', edunew)



    def test_can_create_a_post_and_retrieve_it_later(self):
    
        self.browser.get('http://127.0.0.1:8000/admin/')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('sam')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('password')
        password.send_keys(Keys.ENTER)

        time.sleep(2)

        self.browser.get('http://127.0.0.1:8000/blog/post/new')
        
        self.assertIn('Sam Harrison', self.browser.title)

        title = self.browser.find_element_by_id('id_title')
        title.send_keys('test blog')
        work = self.browser.find_element_by_id('id_text')
        work.send_keys('test test test')

        button = self.browser.find_element_by_id('submitbtn')
        button.click()

        self.browser.get('http://127.0.0.1:8000/blog/')

        time.sleep(2)

        titlesaved = self.browser.find_element_by_id('title')
        self.assertTrue('test blog', titlesaved)

        textsaved = self.browser.find_element_by_id('text')
        self.assertTrue('test test test', textsaved)


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  