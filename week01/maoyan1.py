#作业：使用requests bs4 爬取猫眼电影的前10个电影名称、电影类型、上映时间，并以UTF-8字符集保存到csv格式文件中
import requests
from bs4 import BeautifulSoup as bs

#猫眼电影详情页面
myurl = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = '__mta=213874603.1593230857124.1593236189937.1593236548833.3; uuid_n_v=v1; uuid=DE193580B82B11EA974289B279A7041D77049705DBBA49EFB163166347C35045; _csrf=7894a7df084a25d4bdedbea302c28dcf89906e105ea0e3bf1ec5db06e8f5ea5d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593230856; _lxsdk_cuid=172f3f59095c8-02376967c9c40f-3e3e5e0e-1fa400-172f3f59095b4; _lxsdk=DE193580B82B11EA974289B279A7041D77049705DBBA49EFB163166347C35045; mojo-uuid=34f4e5bc4a8d18127c6caa88a9dcf79b; mojo-session-id={"id":"d855c066c2dbaeb0af242c9e0dcee270","time":1593350475025}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593350475; __mta=213874603.1593230857124.1593236548833.1593350475212.4; _lxsdk_s=172fb16ae68-d46-2f7-c7b%7C%7C3'
header = {'user-agent':user_agent, 'Cookie' : cookie}


response = requests.get(myurl,headers=header)
# print(response.text)
bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
allHoverInfo = bs_info.find_all('div', attrs={'class': 'movie-hover-info'})
mylist = []
for i in range(10):
    info = allHoverInfo[i]
    for detail in info.find_all('div', attrs = {'class':'movie-hover-title movie-hover-brief'}):
        film_name = detail.get('title')
        filmType = detail.text
        filmType.strip()
        filmTime = info.find_all('div', attrs = {'class':'movie-hover-title'})[1].text

        # #电影名称
        # print(film_name)
        # #电影类型
        # print(filmType)
        # #上映时间
        # print(filmTime)
        mylist.append(film_name)
        mylist.append(filmType)
        mylist.append(filmTime)

import pandas as pd

maoyan = pd.DataFrame(data = mylist)
print(mylist)
# windows需要使用gbk字符集
maoyan.to_csv('./maoyan.csv', encoding='gbk', index=False, header=False)

 

      

