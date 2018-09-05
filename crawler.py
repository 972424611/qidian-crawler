import requests
from bs4 import BeautifulSoup
import threading

import deal

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    j = int(threading.current_thread().name)
    #每个线程爬取的页面数
    page = 100
    if j == 1:
        k = 1
        p = page + k
    else:
        k = j * page - page + j - 1
        p = k + page + 1
    for i in range(k, p):
        url = "https://www.qidian.com/all?page=" + str(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        deal.target(soup)