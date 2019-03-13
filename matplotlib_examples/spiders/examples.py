# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import ExampleItem
import browser_cookie3
from foo.config import keywords_dict, urls_dict


def assi_value(kw, pn,ur):
    global page_num
    page_num = pn
    page_num = int(page_num)
    global url_opera
    url_opera = urls_dict[ur]
    global key_word_list
    key_word_list = keywords_dict[kw]


url_sourse = 'http://symobi.zhongsou.com/Material/Keyword?searchKeyword={}&page={}'
# 用来获取关键词的界面


"""下面的才是真正的爬虫"""


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = []
    start_urls = ['http://symobi.zhongsou.com/Interest/index']
    chrome_cookie=browser_cookie3.chrome()

    def start_requests(self):
        yield scrapy.Request(url_opera, meta={'cookiejar':'chrome'})

    def parse(self, response):
        for i in range(page_num):
            for k in range(len(key_word_list)):
                yield scrapy.Request(url_sourse.format(key_word_list[k], i), meta={'cookiejar':'chrome'}, callback=self.main_parse)

    def main_parse(self, response):
        le = LinkExtractor(restrict_css='div.all_member table.sy_table')
        print(len(le.extract_links(response)))
        for link in le.extract_links(response):
            examples = ExampleItem()
            examples['url_examples'] = [link.url]
            yield examples






