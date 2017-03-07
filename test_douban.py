# _*_ coding: utf-8 _*_

"""
test_demos.py by xianhu
"""

import re
import spider
import pymysql
import logging
import requests
from bs4 import BeautifulSoup
from doubanrat import MovieFetcher, MovieParser
def read_user_dict():
    userfile="user_dict.txt"
    infile=open(userfile,'r')
    userlist=[]
    for item in infile.readlines():
        userlist.append(item.strip())
    infile.close()
    return userlist

def get_douban_movies(urls, ind):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        "Host": "movie.douban.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN, zh; q=0.8, en; q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cookie": "bid=Yd7ONilb_ac"
    }

    # 获取初始url
    all_urls = urls
    # 构造爬虫
    dou_spider =spider.WebSpider(MovieFetcher(),MovieParser(max_deep=-1),spider.Saver(save_pipe=open("out_spider_thread%d.txt"%(ind), "w")), spider.UrlFilter())
    for tag, url in all_urls:
        dou_spider.set_start_url(url, ("index", tag), priority=1)
    dou_spider.start_work_and_wait_done(fetcher_num=5)
    return


if __name__ == "__main__":
    logging.basicConfig(filename="logger.log",level=logging.WARNING, format="%(asctime)s\t%(levelname)s\t%(message)s")
    userlist=read_user_dict()
    testurl=[['test','http://movie.douban.com/people/'+'52518341'+'/collect?start=0&sort=rating&rating=all&filter=all&mode=list']]
    get_douban_movies(testurl,0)
"""
    for i in userlist[:5]:
        cururl=[]
        url="http://movie.douban.com/people/"+i.strip()+"/collect?start=0&sort=rating&rating=all&filter=all&mode=list"
        cururl.append([i,url])
        get_douban_movies(cururl,0)
"""
