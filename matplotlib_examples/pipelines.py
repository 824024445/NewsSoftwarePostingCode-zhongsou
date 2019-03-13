# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Url_ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


# class JsonWithEncodingPipeline(object):
#     def __init__(self):
#         self.filename = open('example.json', 'w', encoding="utf-8")
#     def process_item(self, item, spider):
#         lines = json.dumps(dict(item), ensure_ascii=False) + ",\n"#确保中文显示正常
#         self.filename.write(lines)
#         return item
#     def spider_closed(self, spider):
#         self.filename.close()

