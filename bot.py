import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Bot():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=100, poll_frequency=1.0)

    def __init__(self, username, password):
        self.browser = Bot.browser
        self.wait = Bot.wait
        self.username = username
        self.password = password

    def login(self):
        self.browser.get('https://instagram.com/')
        user = self.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
        for i in self.username:
            user.send_keys(i)
            time.sleep(random.uniform(0.1, 0.5))

        passwd = self.wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
        for i in self.password:
            passwd.send_keys(i)
            time.sleep(random.uniform(0.1, 0.5))

        time.sleep(random.randint(1, 4))

        login = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        login.click()
        time.sleep(5)
