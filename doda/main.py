from GetDitail import get_detil
from GetUrl import get_url
from GetUrl import replace_url
from GetUrl import get_sear_url
from ExportExcel import export_xlsx
import time


#検索urlの取得
##url = "https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&ar=3&so=50&tp=2&page=1"
url = "https://doda.jp/DodaFront/View/JobSearchList.action?ss=1&ci=011002%2C231002%2C341002%2C401307&pic=1&ds=0&so=50&tp=2"
list_page_sear = get_sear_url(url)


num = 1
list_output = []
for i in list_page_sear:
    links = get_url(i)
    
    for link in links:
        url = replace_url(link)
        #必要項目を取る
        output = get_detil(url)
        #電話番号複数対策
        list_tell = output[1].split(",")
        #print(list_tell)
        if len(list_tell) > 1:
            for tell in list_tell:
                copy_list = output.copy()
                copy_list[1] = tell
                #print(output)
                list_output.append(copy_list)
        else:
            list_output.append(output)
    
    print(num)
    num += 1
    
export_xlsx(list_output)
