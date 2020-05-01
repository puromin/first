#検索urlを取得する

"""
#https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&ar=3&so=50&tp=2&page=3
#これをベースに考える
#arがエリアを表しており、関東は3
"""


import requests
from bs4 import BeautifulSoup
import re

#soupの基本部分
def get_soup(url):
    """URLのSoupを取得する"""
    html = requests.get(url)
    return BeautifulSoup(html.content, "html.parser")

def get_url(url):
    soup = get_soup(url)
    res1 = soup.find_all("h2", class_ = "title clrFix")
    
    #print(res1)

    list_url = []
    for res in res1:
        res2 = res.find("a")
        row_url = res2.get("href")
        list_url.append(row_url)
    

    return list_url

get_url("https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&ar=3&so=50&tp=2&page=1")

def replace_url(url):
    url = url.replace("/-tab__pr/", "/-tab__jd/-fm__jobdetail/-mpsc_sid__10/")

    return url


#page数を算出する
def num_page(url):
    soup = get_soup(url)
    num = soup.find("span", class_ = "number").text
    #予想されるページ数を算出する
    num_page = int(num.strip()) // 50 + 1


    return num_page

def get_sear_url(url):
    #ページリンクのリストを作成
    list_sea = []
    #検索該当数を代入
    num = num_page(url)
    #検索ページの不変部分
    join_sea_head = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&ar=3&so=50&tp=2&page="
    for i in range(1,num):#動作確認のため、第二引数はnum
        link_sea = join_sea_head + str(i)
        list_sea.append(link_sea)
    
    return list_sea