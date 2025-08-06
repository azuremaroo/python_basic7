import requests # 웹페이지 소스 정보를 요청하는 라이브러리
from bs4 import BeautifulSoup  # 웹소스를 파이썬에서 분석할수 있도록 지원해주는 라이브러리
#import re # 정규표현식 모듈(패키지)
#
#
url = 'https://www.jobkorea.co.kr/Search/?stext=ai%20%EA%B0%9C%EB%B0%9C'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=headers)  # 웹페이지 요청

html = r.text  # r.content Or r.text : 웹페이지 형태
print(html)  #  웹페이지 정보 획득
#
soup = BeautifulSoup(html, 'lxml')  # 파서 지정
# #
# # # 위 방법과 다른 find_all(), find() 메서드 활용
# # find_all() ==> 찾은 tag 정보를 list 형태로 반환
newtitlesoup = soup.find_all(class_ = 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1')

# print(len(newtitlesoup))
# print(newtitlesoup[0].text)
newtitlelist = []
for news in newtitlesoup:
    #print( news.text )
    newtitlelist.append(news.text)
print(newtitlelist)

import pandas as pd
newsdf = pd.DataFrame({'NewsTitle':newtitlelist})
print(newsdf)

newsdf.to_excel("newstitle.xlsx")