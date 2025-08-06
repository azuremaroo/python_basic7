import numpy as np
import pandas as pd
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

# population_in_seoul.xls 파일 읽어서 DataFrame 객체 생성
popdf = pd.read_excel("population_in_seoul.xls") # 엑셀파일을 읽어와서 DataFrame 객체로 생성
print(popdf)

print('='*80)
# 특정 파일을 읽어와서 DataFrame 객체를 생성했으면 꼭 DataFrame 정보를 확인
popdf.info() # 정보확인(컬럼 정보, 인덱스 정보, 결측치, 데이터 타입 등)

# 합계 행과 고령자 컬럼 삭제
print('='*80)
popdf.drop([0], inplace=True)
popdf.drop(['고령자'], axis=1, inplace=True)
print(popdf)

# 특정 컬럼 기준으로 결측치를 찾자(검색)
# ==> isnull() : 결측치면 True, 결측치가 아니면 False 불린배열 생성
# print(popdf['남자'].isnull())
# print(popdf.loc[popdf['남자'].isnull(), :]) # 남자 컬럼 기준 결측치인 항목만 추출
# print('='*80)

# print(popdf['여자'].isnull())
print('='*80)
print(popdf.loc[popdf['여자'].isnull(), :]) # 남자 컬럼 기준 결측치인 항목만 추출
# how = 'any' ==> 해당 행에 결측치가 하나라도 있으면 삭제해
# how = 'all' ==> 모든 행이 결측치 일 때 해당행 삭제해
popdf.dropna(axis=0,how='any', inplace=True)
print(popdf)

# 인덱스를 초기화하자 ==> reset_index()
# 디폴트 기능 ==> 기존 인덱스를 컬럼열로 올려버리고 인덱스를 새로 초기화
# drop=True : 기존 인덱스는 삭제하고 인덱스를 새롭게 초기화(index 컬럼이 추가됨)
popdf.reset_index(drop=True, inplace=True)
print(popdf)

# 자치구 기준 ==> 광진구, 도봉구, 구로구, 서초구, 강동구 인 행만 추출
print('='*80)
# pd.concat([df1, df2, ...]) 여러 df 객체 합치기
# sub1 = popdf.loc[ popdf['자치구'] == '광진구', : ]
# sub2 = popdf.loc[ popdf['자치구'] == '도봉구', : ]
# sub3 = popdf.loc[ popdf['자치구'] == '구로구', : ]
# subdf = pd.concat([sub1, sub2, sub3])
# print(subdf)

subset = popdf.loc[ popdf['자치구'].isin(['광진구', '도봉구', '구로구', '서초구', '강동구']), : ]
print(subset)

# 특정 컬럼데이터를 인덱스로 설정 ==> set_index()
print('='*80)
subset.set_index('자치구', inplace=True)
print(subset)

# subset DataFrame 을 막대 차트로 시각화 하면 한눈에 크기를 비교할 수 있다!!
# 시각화 라이브러리 ==> matplotlib, seaborn, plotly
# pandas DataFrame 에 matplotlib 기능을 내장해서 자체 시각화가 가능

# subset.plot.bar(rot=15) # 현재 DataFrame 정보를 막대 차트로 메모리에 plot(렌더링) 해라!!
# plt.show()

sns.barplot(data=subset, x=subset.index, y='남자', palette='coolwarm')
plt.show()
