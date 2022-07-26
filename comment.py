import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# browser = webdriver.Chrome("C:/Users/ariya/Desktop/projects/insta-project/chromedriver.exe")
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


def comment_on_account(*account):
    for account in account:
        browser.get(f'https://instagram.com/{account}/')
        action = ActionChains(browser)
        rand_num = random.uniform(2.3, 4.2)
        time.sleep(5)
        viewed_posts = []
        browser.implicitly_wait(20)
        posts = browser.find_elements(By.CLASS_NAME, '_aagv')
        for post in posts:
            if post not in viewed_posts:
                action.click(post).perform()
                browser.implicitly_wait(20)
                comment = browser.find_element(By.XPATH, '//*[@class="_aamx"]').click()
                comment_box = browser.find_element(By.CSS_SELECTOR, 'textarea._ablz')
                text = 'متن آزمایشی'
                for c in text:
                    comment_box.send_keys(c)
                    time.sleep(random.uniform(0.1, 0.3))
                comment_box.submit()
                time.sleep(rand_num)
                viewed_posts.append(post)
                browser.back()
            else:
                browser.back()


comments = [
    'hello',
    'how are you?',
    'i am ...',
    'who you are?',
    'are you executive?',
    "i know you are not procrastinator.",
]


def comment_on_hashtag(*hashtag, comment_count=1, post_count=1):
    for hashtag in hashtag:
        browser.get(f'https://instagram.com/explore/tags/{hashtag}/')
        action = ActionChains(browser)
        time.sleep(5)
        rand_num = random.uniform(4.3, 7.2)
        browser.implicitly_wait(20)
        posts = browser.find_elements(By.CLASS_NAME, '_aagv')
        for n in range(post_count):
            action.click(posts[n]).perform()
            time.sleep(5)
            try:
                restricted_commenting = browser.find_element(By.XPATH, '//div[text()="Comments on this post have been limited."]')
                browser.back()
            except:
                comment = browser.find_element(By.XPATH, '//*[@class="_aamx"]').click()
                time.sleep(3)
                comment_box = browser.find_element(By.XPATH, '//*[@aria-label="Add a comment…"]')
                for n in range(comment_count):
                    text = comments[random.randint(0, len(comments) - 1)]
                    print(text)
                    for c in text:
                        comment_box.send_keys(c)
                        time.sleep(random.uniform(0.1, 0.3))
                    comment_box.submit()
                    time.sleep(rand_num)
                browser.back()


login(browser, username, password)
comment_on_hashtag('programming', comment_count=3, post_count=2)
