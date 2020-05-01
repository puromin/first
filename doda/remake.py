import re

#取り出したデータを整える
def remake(lists):
    #["会社名", "電話番号", "掲載url", "掲載期間", "設立", "企業url", "所在地", "従業員数"]
    terms = lists[3]
    #terms: 2020/3/23（月）       ～2020/4/19（日）のような形
    columns = terms.split("～")

    start_time = re.sub(r"（.+", "", columns[0])
    lists.append(start_time)
    end_time = re.sub(r"（.+", "", columns[1])
    lists.append(end_time)

    #郵便番号を削除する
    lists[6] = re.sub(r"〒\d{3}-\d{4}", "", lists[6])


    #print(lists)
    return lists
   

list_sample = ["株式会社AdeaA", "000-000-0000", "http:", "2020/3/23（月）～2020/4/19（日）", "1996年", "https","福岡本社】福岡県福岡市博多区上牟田1-19-21【東京本社】東京都中央区日本橋茅場町1-7-1", "2000名"]

remake(list_sample)
