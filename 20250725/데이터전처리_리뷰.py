import numpy as np
import pandas as pd
import re
import seaborn as sns

# === matplotlib 에 한글 폰트 적용하기 시작 ===
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")
# === matplotlib 에 한글 폰트 적용하기 끝 ===

# === pnadas 출력 제어 옵션 설정 시작 ===
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
# === pnadas 출력 제어 옵션 설정 끝 ===

mydf = pd.read_excel("youtube_rank_1000.xlsx")
# print(mydf)
mydf.info() # info() 를 통해 컬럼 데이터 타입과 결측치 유무 확인 필수
print(mydf.head()) # 데이터가 많을 경우 처음부터 5개(기본값)만 출력

del mydf['Subscriber'] # 필요 없는 컬럼 제거
print(mydf.head())

def VideoDataControl(arg): # string 데이터를 머신러닝을 위해 정수형인 int 로 변경
    # return int(arg.replace('개', '').replace(',', '')) # 문자열객체 활용해서 필터링
    return re.sub('[,개]', '', arg) # 정규 표현식 활용해서 필터링

mydf['Video'] = mydf['Video'].apply(VideoDataControl).astype('int64') # Video 컬럼 데이터가 순차적으로 함수에 전달되서 함수에 기능이 적용됨
# mydf['Video'] = mydf['Video'].astype('int64')
mydf.info()

print('='*80)

def view_modify(arg): # 문자열 함수를 이용
    return int(arg.replace('억', '').replace('만', '0000'))

mydf['View'] = mydf['View'].apply(view_modify)


print(mydf['View'].head(10))
mydf.info()

# View 데이터 기준 10000000 View 이상의 데이터만 추출
# subset = mydf.loc[mydf['View'] > 500000000, :].copy()
# print(subset.head())
# subset.info()

# View 데이터 기준 상위 10개 데이터만 추출
# 정렬(내림차순), 특정 컬럼은 by 파라미터에 (정렬 우선순위 순서대로) 설정
# ascending : 내림차순(False), 오름차순(True) 결정
mydf.sort_values(by=['View', 'Video'], ascending=False, inplace=True) # 특정 컬럼 데이터 기준으로 정렬해줘!!
ViewDataTop10 = mydf.head(10).copy()
print(ViewDataTop10)

# ViewDataTop10 DataFrame 객체를 활용해서 막대 차트 시각화 함
# seaborn 의 barplot() 을 활용
# x 축은 ChannelName
# y 축은 View 컬럼 데이터 활용

# ViewDataTop10.set_index('View', inplace=True)
# sns.barplot(data=ViewDataTop10, x=ViewDataTop10.index, y='ChannelName', palette='coolwarm')
fig = plt.figure( figsize=(15,8) ) # 차트 창 크기 설정
sns.barplot(data=ViewDataTop10, x='ChannelName', y='View', palette='coolwarm') # 메모리에 렌더링
plt.show() # 화면에만 출력
plt.savefig('ViewTop10.jpg') # 이미지 파일로 저장까지


