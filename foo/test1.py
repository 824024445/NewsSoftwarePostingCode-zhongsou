#!/usr/bin/env python
import json
import random


f = open("files/example_duanzi.json", "r+")
d = f.read()
d = d.replace("][", ",")
start_urls = json.loads(d)
urls = list(reversed(start_urls))
random.shuffle(urls)