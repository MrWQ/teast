# -*- coding: utf-8 -*-
# @Time : 2022/7/20 10:24
# @Author : ordar
# @Project : teast
# @File : t_sploitus.py
# @Python: 3.7.5
import requests
import cloudscraper

url = "https://sploitus.com/top"
scraper = cloudscraper.create_scraper()
resp = scraper.get(url)

# resp = requests.get(url)
out = ""
out = out + str(resp.status_code) + '\n'
out = out + str(resp.headers) + '\n'
out = out + str(resp.text) + '\n'
print(out)
with open("sploitus.log", 'w') as f:
    f.write(out)

