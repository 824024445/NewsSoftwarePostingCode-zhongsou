#!/usr/bin/env python
from selenium import webdriver
import time
import json
import random
from foo.config import cookies_dict, urls_dict, send_number
map_lists = ["经济圈", "摄影圈", "男人圈", "社会百科", "内涵段子"]


def add_digest(record):
    browser = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    browser.get('http://symobi.zhongsou.com')
    browser.add_cookie(cookies_dict[map_lists[record]])
    browser.get(urls_dict[map_lists[record]])
    time.sleep(2)
    try:
        browser.find_element_by_css_selector("body > div.comhelper_sycontent.mt25 > div > div.sy_treefl.w210.b_fff.fl > div.sy_treelist > div:nth-child(1) > ul > li:nth-child(2) > a").click()
        time.sleep(3)
        t = 0
        # for i in range(1,100):
        judge = browser.find_element_by_css_selector("#contentList > div:nth-child(4) > ul.operate > li:nth-child(3)")
        judge.click()
        time.sleep(2)
        # if not browser.find_element_by_css_selector("#contentList > div:nth-child(3) > div > i"):
        #     judge.click()
        #     time.sleep(2)

        print("11111")
    except:
        print("2222")


if __name__ == "__main__":
    add_digest(1)


#contentList > div:nth-child(3)
#contentList > div:nth-child(3) > ul.operate > li:nth-child(3)
#contentList > div:nth-child(1) > ul.operate > li:nth-child(3)
#contentList > div:nth-child(1) > div > i.jing
