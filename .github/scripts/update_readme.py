import re
import urllib.parse
import os

rand_moe = os.environ.get('RAND_MOE', '')
rand_fox = os.environ.get('RAND_FOX', '')
quote_cn = os.environ.get('QUOTE_CN', '喵喵喵好像出错了 ~nya')
quote_en = os.environ.get('QUOTE_EN', 'Meow something went wrong ~nya')
quote_from = os.environ.get('QUOTE_FROM', '云汀')

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 直接 quote，不用 replace
cn_encoded = urllib.parse.quote(quote_cn)
en_encoded = urllib.parse.quote(quote_en)

# ... 后面不变
