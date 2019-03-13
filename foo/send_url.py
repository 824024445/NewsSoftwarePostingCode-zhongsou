#!/usr/bin/env python
from selenium import webdriver
import time
import json
import random
from foo.config import cookies_dict, urls_dict, send_number
map_lists = ["经济圈", "摄影圈", "男人圈", "社会百科", "内涵段子"]


def send_url(record):
    rec = open("files/record.json", "a", encoding="utf-8")
    # 打开通过爬虫爬取得帖子url
    f = open("files/example{}.json".format(record), "r")
    d = f.read()
    d = d.replace("][",",")
    start_urls = json.loads(d)
    urls = list(reversed(start_urls))
    random.shuffle(urls)
    # 从日期早的开始发，所以把url倒过来
    print(len(urls))
    f.close()
    browser = webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    browser.get('http://symobi.zhongsou.com')
    browser.add_cookie(cookies_dict[map_lists[record]])
    browser.get(urls_dict[map_lists[record]])
    t = 0
    for i in range(0,len(urls)):
        # 如果要url接力的话，吧上次URL的数量输在len之前就好
        browser.get('http://symobi.zhongsou.com/Blog/edit?url={}&sorce=Material'.format(urls[i]["url_examples"][0]))
        time.sleep(2)
        try:
            iframe = browser.find_element_by_class_name('ke-edit-iframe')
            browser.switch_to_frame(iframe)
            find_img = browser.find_element_by_css_selector('body.ke-content')
            find_img.find_element_by_tag_name('img')
            # 查找img元素，找到之后要跳出iframe
            browser.switch_to_default_content()
            browser.find_element_by_css_selector('a.sy_bn,bn_1,fl,w80').click()
            time.sleep(1)
            try:
                browser.find_element_by_css_selector('div#msgPic i')
                time.sleep(1)
            except:
                if record == 0:
                    if t > send_number[map_lists[record]]:
                        break
                elif record == 1:
                    if t > send_number[map_lists[record]]:
                        break
                elif record == 2:
                    if t > send_number[map_lists[record]]:
                        break
                elif record == 3:
                    if t > send_number[map_lists[record]]:
                        break
                elif record == 4:
                    if t > send_number[map_lists[record]]:
                        break
                time.sleep(8)
                t += 1
        except:
            time.sleep(1)
    rec.write(time.strftime("%Y-%m-%d %H:%M:%S")+ map_lists[record]+ "发送:"+ str(t)+ "个帖子\n")
    rec.close()

