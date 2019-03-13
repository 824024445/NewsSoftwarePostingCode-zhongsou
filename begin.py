#!/usr/bin/env python
from scrapy import cmdline
from matplotlib_examples.spiders.examples import assi_value
'''
获取url
其中，参数arg，0代表经济圈，1代表摄影圈，2代表男人圈，3代表社会百科圈，4代表内涵段子圈
引用的函数assi_value是用来设定爬虫的参数，分别为关键词，获取帖子页数以及对应圈子的url
'''
map_lists = ["经济圈", "摄影圈", "男人圈", "社会百科", "内涵段子"]


def obtain_url(arg):
    if arg != 4:
        f = open("files/example{}.json".format(arg), "w")
        f.truncate()
        f.close()
        assi_value(map_lists[arg], 15, map_lists[0])
        cmdline.execute("scrapy crawl examples -o files/example{}.json".format(arg).split())
    else:
        assi_value(map_lists[arg], 15, map_lists[0])
        cmdline.execute("scrapy crawl examples -o files/example{}.json".format(arg).split())

