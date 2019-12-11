# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:47:15 2019

@author: 佘建友
"""
#引入随机模块
import requests,random
base_url = 'https://www.baidu.com/'
#构建代理ip列表，里面一般包含http与https两种协议的代理ip。为了适应不同的网站,
#该模块会根据所要访问的网站的协议类型自动选择合适的ip
procxy = [
         {'http':'HTTP://121.52.208.200:808',
         'https':'HTTPS://111.177.106.231:9999'},
         {'https':'HTTPS://192.168.1.110',
         'http':'HTTP://192.168.1.110'
         },
         {'http':'HTTP://180.119.68.10:9999',
          'https':'HTTPS://123.169.34.240:4366'},
         {'https':'HTTPS://171.35.223.182'},
          {'https':'HTTPS://117.69.200.125'}
                 
        ]

#随机选择列表中的字典，直到匹配上可以使用的ip
http = random.choice(procxy)
#Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
#timeout是超时时间，因为连接某些代理比较慢，设置超时时间避免等待时间过长
response = requests.get(url=base_url,proxies=http,timeout=20)
contents = response.content.decode('utf-8')
print(contents)