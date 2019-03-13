#!/usr/bin/env python
from selenium import webdriver
import time
import json
import random



username = ["17786431817", "17786463817", "15539143753", "18730222329"]
passwd = ["wd123456..", "123456..", "950817lqy"]
def acquir_cookie_url(arg):
    browser = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    browser.get('http://symobi.zhongsou.com')
    # browser.add_cookie({'domain': '.zhongsou.com', 'httpOnly': False, 'name': 'sy_interest_id', 'path': '/', 'secure': False, 'value': '143'})
    # browser.get('http://symobi.zhongsou.com')
    elem1 = browser.find_element_by_id("username")
    elem2 = browser.find_element_by_id("password")
    if arg == 1:
        elem1.send_keys(username[0])
        elem2.send_keys(passwd[0])
    elif arg == 2:
        elem1.send_keys(username[1])
        elem2.send_keys(passwd[2])
    elif arg == 3:
        elem1.send_keys(username[2])
        elem2.send_keys(passwd[1])
    elif arg == 4:
        elem1.send_keys(username[3])
        elem2.send_keys(passwd[0])
    time.sleep(10)
    x = browser.get_cookies()
    print(x)
    time.sleep(10)


if __name__ == "__main__":
    # for i in range(4):
    #     print(i+1)
    #     acquir_cookie_url(i+1)
    # 经济圈
    # acquir_cookie_url(1)
    # 摄影圈
    # acquir_cookie_url(2)
    # 男人圈和社会百科圈
    # acquir_cookie_url(3)
    # 内涵段子圈
    acquir_cookie_url(4)



