import requests
from bs4 import BeautifulSoup
import re
import time
from remake import remake

#soupの基本部分
def get_soup(url):
    """URLのSoupを取得する"""
    html = requests.get(url)
    return BeautifulSoup(html.content, "html.parser")

#タイムエラーに対する繰り返し処理
num_retry = 3

def get_detil(url):
    for i  in range(1, num_retry + 1):
        try:
            soup = get_soup(url)
        except:
            print("errorが発生しました."+ str(i) + "回目")
            time.sleep(i * 30)
        else:
            break

    res1 = soup.find_all("dl", class_="band_title")
    try:
        row_tell = res1[3].text
        list_tell = re.findall(r"0\d{1,3}-\d{1,4}-\d{1,4}", row_tell)
        tell = ",".join(list_tell)
    except:
        tell = ""

    #掲載期間
    term_soup = soup.find("div", class_ = "publishingSchegulePeriod")
    term = term_soup.find("p").text
    term = term.replace("掲載予定期間：", "")


    #会社名
    res_name = soup.find_all("div", class_ = "head_title")
    name_com = res_name[0].find("h1").text
    name_com = name_com.strip()
    #print(name_com)

    #詳細情報
    #テーブルのデータを取得
    detail_soup = soup.find("table", id = "company_profile_table")
    rows = detail_soup.find_all("tr")

    #thとtdを辞書にする
    dic_list = {}
    for row in rows:
        th = row.find("th").text
     
        td = row.find("td").text.strip()
        td = "".join(td.split())

        dic_list[th] = td
    
    #print(dic_list)
    list_com = [name_com, tell, url, term]
    list_columns = ["設立", "企業URL", "所在地", "従業員数"]
    for column in list_columns:
        if column in dic_list:
            list_com.append(dic_list[column])
        else:
            list_com.append("")

    #バッチ処理
    time.sleep(2)

    #print(list_com[0])
    list_com = remake(list_com)
    return list_com

#get_detil("https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3003942388/-tab__jd/-fm__jobdetail/-mpsc_sid__10/-tp__2/")