import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome("C:/Users/ariya/Desktop/projects/insta-project/chromedriver.exe")
browser.maximize_window()
username = 'muslim344421'
password = '@#Mu1234'
wait = WebDriverWait(browser, 100)


def login(browser, username, password):
    browser.get('https://instagram.com/')
    user = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
    for i in username:
        user.send_keys(i)
        time.sleep(random.uniform(0.1, 0.5))

    passwd = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    for i in password:
        passwd.send_keys(i)
        time.sleep(random.uniform(0.1, 0.5))

    time.sleep(random.randint(1, 4))

    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login.click()
    time.sleep(5)


def view_story(*pages_id):
    for page in pages_id:
        browser.get(f'https://instagram.com/{page}/')
        browser.implicitly_wait(100)
        try:
            story = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="_aarf _aarg"]'))).click()
            browser.implicitly_wait(100)
            not_seen = browser.find_elements(By.XPATH, '//*[@class="_ac3o"]')
            rand = random.uniform(1.0, 2.3)
            sleep = time.sleep(rand)
            print('sleep: ' + str(rand))
            next = browser.find_element(By.CLASS_NAME, '_9zm2').click()
            try:
                browser.implicitly_wait(100)
                seen = browser.find_elements(By.XPATH, '//*[@class="_ac3p"]')
                seen = len(seen)
            except:
                seen = 0

            finally:
                while not (len(not_seen) == (seen + 1)):
                    seen += 1
                    print('seen: ' + str(seen))
                    rand = random.uniform(1.0, 2.3)
                    sleep = time.sleep(rand)
                    print('sleep: ' + str(rand))
                    next = browser.find_element(By.CLASS_NAME, '_9zm2').click()
        except:
            print('this id has no story today! ')

        finally:
            time.sleep(5)


login(browser, username, password)
view_story('web_burger.ir', 'd_krystal_b', 'nimagram_admin')

# view story based on account id
