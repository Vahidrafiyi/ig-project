import random
import time

import pandas as pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument('--lang=en-US')
option.add_argument('--window-size=1200,1000')

browser = webdriver.Chrome(options=option)
browser.maximize_window()
username = 'muslim344421'
password = '@#Mu1234'
wait = WebDriverWait(browser, 100)


def login(browser, username, password):
    # browser.delete_all_cookies()
    browser.get('https://instagram.com/')
    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # for cookie in cookies:
    #     # cookie['domain'] = 'instagram.com'
    #     print(cookie)
    #     browser.add_cookie(cookie)
    # time.sleep(2)
    # browser.get('https://instagram.com/vahidrafiyi/')
    # browser.refresh()
    # print(browser.get_cookies())
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
    #


def get_reach(page, reach='followers'):
    reach_list = []
    browser.get(f'https://www.instagram.com/{page}/{reach}/')
    browser.implicitly_wait(100)
    f = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_aano')))
    d = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_aaey')))
    # end_scroll = browser.execute_script('return arguments[0].scrollHeight', d)
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(2)
        # scroll down and retrun the height of scroll
        ht = browser.execute_script(""" 
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight; """, f)

    # while True:
    #     print('end scroll: ' + str(end_scroll))
    #     browser.execute_script(
    #         'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].scrollHeight;',
    #         f)
    #     time.sleep(random.randint(3,5))
    #     scroll_height = browser.execute_script('return arguments[0].scrollHeight', d)
    #     print('scroll height: ' + str(scroll_height))
    #     if scroll_height == end_scroll:
    #         break
    #     else:
    #         end_scroll = scroll_height


    reaches = d.find_elements(By.CLASS_NAME, '_aaei')
    for li in reaches:
        div1 = li.find_element(By.CLASS_NAME, '_aaem')
        div2 = div1.find_element(By.CLASS_NAME, '_aaen')
        div3 = div2.find_element(By.CLASS_NAME, '_aaeo')
        div4 = div3.find_element(By.CLASS_NAME, '_aaep')
        span = div4.find_element(By.CLASS_NAME, '_aap6')
        span2 = span.find_element(By.CLASS_NAME, '_aade').text
        # id = id[:-1:].split('https://instagram.com/')[1]
        reach_list.append(span2)
    return reach_list


def get_reach_detail_list(insta_page, excel_name):
    output = {}
    followers = get_reach(insta_page, 'followers')
    time.sleep(random.randint(1, 5))
    followings = get_reach(insta_page, 'following')
    not_followed_us = []
    for following in followings:
        if following not in followers:
            not_followed_us.append(following)
    output[f'{insta_page} followers'] = followers
    output[f'{insta_page} followings'] = followings
    output[f' فالووینگ هایی که {insta_page} را دنبال نکرده اند '] = not_followed_us
    data = pandas.DataFrame.from_dict(output, orient='index')
    data = data.transpose()
    writer = pandas.ExcelWriter(f'{excel_name}.xlsx')
    data.to_excel(writer)
    writer.save()


login(browser, username, password)
# pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
# browser.quit()
time.sleep(5)
get_reach_detail_list('web_burger.ir', 'webburger_reachs')
