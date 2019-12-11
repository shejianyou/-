# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:12:40 2019

@author: 佘建友
"""
import time
import json
import requests
from urllib.parse import urlencode


proxy = '114.239.2.161'
proxies = {
        'http':'http://'+proxy,
        'https':'https://'+proxy,
        }

def get_newslist(page):
    """
    this method helps ueser to get the list of news
    the param is the numeber of page
    :return a geneator
    """
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
    params = {
        'q': 'Xinjiang',
        'size': '10',
        'from': 10*(page-1),
        'page': page,
        }
    url = 'https://search.api.cnn.io/content?'+urlencode(params)
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        result = r.json()
        datas = result.get('result')
        try:
            for data in datas:
                yield{
                'headline':data.get('headline'),
                'lastPublishDate':data.get('lastPublishDate'),
                'section':data.get('section'),
                'url':data.get('url'),
                'body':data.get('body'),
                }
        except TypeError:
            page += 1
            get_newslist(page)
    else:
        print('抓取失败')


def save_text(item):
    """
    this function save info of every new by special formate
    """  
    with open(r'C:\Users\23909\Desktop\CNN新疆.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False) + '\n')
            
def main():
    """
    the access of the whole 
    """
    for page in range(0,38):
        items = get_newslist(page)
        for item in items:
            print('正在打印第',page,'页的信息!!!')
            print(item)
            save_text(item)
        time.sleep(3)


        
