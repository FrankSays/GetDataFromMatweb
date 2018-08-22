# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
import time
import random

class Alloy_Target:

    def __init__(self,name,url):
        self.name=name
        self.url=url
#爬虫代码
def reptilian(AT,ct):
# 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
# 代理隧道验证信息
    proxyUser = "HU5W3F332U8B198D"
    proxyPass = "A018D7750EF20402"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }
    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }


#request配置加爬虫
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
    req=requests.get(url=AT.url,headers=headers,proxies=proxies)
    html=req.text
    bf=BeautifulSoup(html)
    table=bf.find_all('table', cellspacing="0")
    trs=BeautifulSoup(str(table)).find_all('tr')
    ulist=[]
#文本处理
    for tr in trs:
        ui = []
        for td in tr:
            r=td.get_text().replace("\xa0","")
            ui.append(r)
        ulist.append(ui)
    ulist = [x for x in ulist if x !=['']]
#写入文件夹
    with open("F:/mdata/"+"AA"+str(ct)+".csv", 'w',newline='', encoding='utf-8') as f1:#存放数据，我写的是F盘下面，可以建立一个文件加存放，改一下路径即可
        writer = csv.writer(f1)
        writer.writerow([AT.name])
        for i in range(len(ulist)):
            writer.writerow(ulist[i])







f=open("C:/Users/Frank/Desktop/output", "r", encoding='UTF-8')#!!!这里output的路径需要根据电脑位置改
line=f.readline()
line=f.readline()#把第一行去掉，有\ufeff
ct=1402
while line:
  ct += 1
  info=line.split("_")
  AT=Alloy_Target(info[0],info[1])
  reptilian(AT,ct)
  print("第"+str(ct)+"个已完成，共1505个")
  #time.sleep(random.randint(1,3))
  line = f.readline()

