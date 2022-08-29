# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:58:08 2022

@author: samsu
"""

from bs4 import BeautifulSoup
import requests

with open('html.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')


#match=soup.title.text
#match=soup.find('div',class_='footer').text
#print(match)

'''
article=soup.find('div',class_='article')
print(article)
headline=article.h2.a.text
print(headline)

summary=article.p.text
print(summary)
'''

articles=soup.find_all('div',class_='article')
for article in articles:
    headline=article.h2.a.text
    print(headline)
    summary=article.p.text
    print(summary)