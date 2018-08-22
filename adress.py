# -*- coding:UTF-8 -*-
import os
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8') #改变标准输出的默认编码

def get_herf(path):
    f = open(path, encoding='UTF-8')
    html = f.read()
    table_all = BeautifulSoup(html)
    table = table_all.find_all('table', class_="tabledataformat t_ablegrid")
    a_bf = BeautifulSoup(str(table[0]))
    a = a_bf.find_all('a')
    for i in range(1, a.__len__()):
        #result.write(a[i].string+"-" + server + a[i].get('href')+"\n")
        print(a[i].string+"_" + server + a[i].get('href'))

if __name__ == "__main__":
    output='F:/output'
    server='http://www.matweb.com'
    dir='C:/Users/Frank/Desktop/MATWEBdata'
    with open(output, 'a') as result:
        if os.path.exists(dir):
            dirs = os.listdir(dir)
            for dirc in dirs:
                get_herf(dir+"/"+dirc)


