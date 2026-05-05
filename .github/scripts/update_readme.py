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

cn_encoded = urllib.parse.quote(quote_cn)
en_encoded = urllib.parse.quote(quote_en)

moe_new = f'<!-- MOE_IMG_START -->\n<p align="center">\n  <img src="https://t.alcy.cc/moez?r={rand_moe}" width="400" alt="萌图" />\n</p>\n<!-- MOE_IMG_END -->'
content = re.sub(r'<!-- MOE_IMG_START -->.*?<!-- MOE_IMG_END -->', moe_new, content, flags=re.DOTALL)

fox_new = f'<!-- FOX_IMG_START -->\n<p align="center">\n  <img src="https://t.alcy.cc/xhl?r={rand_fox}" width="400" alt="小狐狸" />\n</p>\n<!-- FOX_IMG_END -->'
content = re.sub(r'<!-- FOX_IMG_START -->.*?<!-- FOX_IMG_END -->', fox_new, content, flags=re.DOTALL)

quote_new = f'<!-- DAILY_QUOTE_START -->\n<p align="center">\n  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=3000&color=FF69B4&center=true&vCenter=true&width=700&lines={cn_encoded};{en_encoded}" alt="Daily Quote" />\n</p>\n\n<p align="center"><b>🎯 中文：</b>{quote_cn}</p>\n<p align="center"><b>🎯 English：</b>{quote_en}</p>\n<p align="center"><sub>— {quote_from}</sub></p>\n<!-- DAILY_QUOTE_END -->'
content = re.sub(r'<!-- DAILY_QUOTE_START -->.*?<!-- DAILY_QUOTE_END -->', quote_new, content, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
