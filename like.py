import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 100)


def login(browser, username, password):
    browser.get('https://www.instagram.com/')
    user = wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
    user.send_keys(username)

    passwd = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    passwd.send_keys(password)

    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login.click()
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
    button.click()
    notification = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@tabindex="0"][2]')))
    notification.click()

def visit_post(browser, url, liked_count=0):
    browser.get(url)
    browser.implicitly_wait(100)
    posts = browser.find_elements(By.CLASS_NAME, '_aagw')
    for post in posts:
        if liked_count >= 3:
            break
        else:
            post.click()
            if wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Unlike"]'))):
                close = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Close"]'))).click()
            else:
                like = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Like"]')))
                print(like)
                like.click()
                close = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Close"]'))).click()
                liked_count += 1
                print(liked_count)


def main():
    login(browser, 'muslim344421', '@#Mu1234')
    tags = [
        'programming',
        'python',
        'django'
    ]
    for tag in tags:
        liked_count = 0
        url = f'https://instagram.com/explore/tags/{tag}'
        visit_post(browser, url, liked_count)
        time.sleep(5)


main()
