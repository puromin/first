import pandas as pd
import time
import datetime

def rename():
    dt_now = datetime.datetime.now()
    name_dt = dt_now.strftime("%m%d%H%M")

    name_hade = "doda_"
    name_end = ".xlsx"


    name_file = name_hade + name_dt + name_end

    #print(name_file)
    return name_file

rename()

 # Xlsx ファイル出力
def export_xlsx(lists):
    #pandasのデータフレームに収納
    df = pd.DataFrame(lists,
                    columns=["会社名", "電話番号", "掲載url", "掲載期間", "設立",
                             "企業url", "所在地", "従業員数", "掲載開始日", "掲載終了日"])
    

    name_file = rename()
    #ファイル名
    df.to_excel(name_file, index = False)

#Asamples = [['株式会社AdeaA', '000-000-0000', 'http:', '2020/3/23（月）～2020/4/19（日）', '1996年', 'https', '福岡本社】福岡県福岡市博多区上牟田1-19-21【東京本社】東京都中央区日本橋茅場町1-7-1', '2000', '2020/3/23', '2020/4/19']]

#export_xlsx(Asamples)