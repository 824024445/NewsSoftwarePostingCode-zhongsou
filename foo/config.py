#!/usr/bin/env python
keywords_dict = {
    "经济圈": ["%E7%BB%8F%E6%B5%8E", "%E9%87%91%E8%9E%8D", "%E8%AF%81%E5%88%B8", "%E8%82%A1%E7%A5%A8", "%e6%8a%95%e8%b5%84"],
    "摄影圈": ["%E6%8B%8D%E7%85%A7", "%E6%91%84%E5%BD%B1", "%E7%85%A7%E7%89%87", "%E7%BE%8E%E6%99%AF"],
    "男人圈": ["%E7%94%B7%E4%BA%BA", "%E5%81%A5%E8%BA%AB", "%E7%94%B7%E7%94%9F", "%E7%AF%AE%E7%90%83"],
    "社会百科": ["%E4%BA%8B%E4%BB%B6", "%E7%8E%B0%E8%B1%A1", "%E6%96%87%E5%A8%B1", "%E7%A7%91%E6%8A%80"],
    "内涵段子": ["%e5%86%b7%e7%ac%91%e8%af%9d","%e8%b6%a3%e5%9b%be","%e5%86%85%e6%b6%b5%e5%9b%be","%e5%86%85%e6%b6%b5%e6%ae%b5%e5%ad%90","%e6%af%8f%e6%97%a5%e4%b8%80%e7%ac%91"]
}

cookies_dict = {
    "经济圈": {'domain': '.zhongsou.com', 'expiry': 1553742703, 'httpOnly': False, 'name': 'qrcode_user_name', 'path': '/', 'secure': False, 'value': '9cd9Z9YSvjzb97G/s+ZSXBjs341LVEFGuPlnt4glAyGK6ZowJimryA'},
    "摄影圈": {'domain': '.zhongsou.com', 'expiry': 1553742803, 'httpOnly': False, 'name': 'qrcode_user_name', 'path': '/', 'secure': False, 'value': '9be3MiE80gpg5wisaHSAQ+3iA71FZbQCOeLZKTGXacvNNYZHMVKJSQ'},
    "男人圈": {'domain': '.zhongsou.com', 'expiry': 1553742873, 'httpOnly': False, 'name': 'qrcode_user_name', 'path': '/', 'secure': False, 'value': 'c3c7gGSfSgdumz+iAdd02azS/QbvLrfRWlCgPK+x0p81FKX5lijUUg'},
    "社会百科": {'domain': '.zhongsou.com', 'expiry': 1553742873, 'httpOnly': False, 'name': 'qrcode_user_name', 'path': '/', 'secure': False, 'value': 'c3c7gGSfSgdumz+iAdd02azS/QbvLrfRWlCgPK+x0p81FKX5lijUUg'},
    "内涵段子": {'domain': '.zhongsou.com', 'expiry': 1553742944, 'httpOnly': False, 'name': 'qrcode_user_name', 'path': '/', 'secure': False, 'value': '0ed01hSK2kLer0c7ZsKJ/jlBwdH5EgtUknzXOP9MugdAgwwB9vi5eA'}
}

urls_dict = {
    "经济圈": 'http://symobi.zhongsou.com/?interest_id=16595&rand=792034338',
    "摄影圈": "http://symobi.zhongsou.com/?interest_id=143&rand=1007072260",
    "男人圈": "http://symobi.zhongsou.com/?interest_id=15268&rand=1696002622",
    "社会百科": "http://symobi.zhongsou.com/?interest_id=18169&rand=640876621",
    "内涵段子": "http://symobi.zhongsou.com/?interest_id=97&rand=790477809"
}

send_number = {
    "经济圈":310,
    "摄影圈": 311,
    "男人圈": 301,
    "社会百科": 250,
    "内涵段子": 308
}
