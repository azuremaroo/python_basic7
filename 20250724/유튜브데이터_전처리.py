import numpy as np
import pandas as pd
import re

# === pnadas 출력 제어 옵션 설정 시작 ===
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
# === pnadas 출력 제어 옵션 설정 끝 ===

youdf = pd.read_excel("youtube_rank_1000.xlsx")
# print(youdf)
# print(youdf.info())


# 문제 : ChannelName 컬럼의 데이터를 전처리
# print(youdf['ChannelName'])
print('='*80)

def channelname_modify(arg):
    return arg.split(' ')[0]

youdf['ChannelName'] = youdf['ChannelName'].apply(channelname_modify)
print(youdf.head(20))

del youdf['Subscriber']
print(youdf.head(10))

# 문제 : View 컬럼 데이터 변경
def view_modify(arg): # 문자열 함수를 이용
    return int(arg.replace('억', '').replace('만', '0000'))

def view_modify_regex(arg): # 정규식 이용
    return re.sub('억', '', arg).replace('만', '0000')

youdf['View'] = youdf['View'].apply(view_modify)
# youdf['View'] = youdf['View'].astype('int64') # astype() 특정 컬럼의 타입 변경

print(youdf['View'].head(10))

