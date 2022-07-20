# -*- coding: utf-8 -*-
# @Time : 2022/7/20 10:24
# @Author : ordar
# @Project : teast
# @File : t_sploitus.py
# @Python: 3.7.5
import requests

url = "https://sploitus.com/top"

resp = requests.get(url)
print(resp.status_code)
print(resp.headers)
print(resp.text)


