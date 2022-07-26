import unittest

from selenium import webdriver

from follow_unfollow_comparision import login


class LoginInstagram(unittest.TestCase):
    def setUp(self):
        self.username = 'muslim344421'
        self.password = '@#Mu1234'
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://instagram.com/')

    def test_login(self):
        login(self.driver, self.username, self.password)
        assert True

    def tearDown(self):
        self.driver.quit()


if '__name__' == '__main__':
    unittest.main()
