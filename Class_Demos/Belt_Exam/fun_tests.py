"""This tests the functionality of our site!"""
from selenium import webdriver
import unittest

# FUNCTIONAL TESTING FOR LANDING PAGE
class NewVisitorTest(unittest.TestCase):
    """This tests the functionality of our landing page."""
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # A user visits our page and sees two forms, asking them to either login or register
    def test_landing_shows_two_forms(self):
        self.browser.get('http://localhost:8000/')
        logform = self.browser.find_element_by_id=('logform')
        regform = self.browser.find_element_by_id=('regform')
        self.assertIsNotNone(logform)
        self.assertIsNotNone(regform)

    # A user fills out a registration form correctly and successfully registers

    # After successful registration, a user is shown their travel dashboard

    # After an invalid registration attempt, a user is redirected to the landing and shown errors

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')