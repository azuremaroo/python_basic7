import numpy as np
import pandas as pd
import re

# === matplotlib 에 한글 폰트 적용하기 시작 ===
import seaborn as sns
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

Controldf = pd.read_excel("반도체_제어_이력.xlsx", index_col=0)
# print(Controldf.head())
# Controldf.info()

# 담당 엔지니어와 비고 컬럼 삭제
Controldf.drop(columns=['담당 엔지니어','비고'], inplace=True)
# print(Controldf.head())


print('='*80)

# 공정 단계를 기준으로 목표값의 평균을 계산해서
# 공정 단계의 목표값의 평균이 가장 높은 것이 무엇인지 막대 차트 시각화 출력

# print(Controldf['공정 단계'].unique())
# grpdf = Controldf.groupby('공정 단계')[['목표값']].agg('mean').sort_values(by=['목표값'], ascending=False, inplace=False)
grpdf = Controldf.pivot_table(index='공정 단계', values='목표값', aggfunc='mean', margins=True)
print(grpdf)

fig = plt.figure( figsize=(15,8) ) # 차트 창 크기 설정
sns.barplot(data=grpdf, x='공정 단계', y='목표값', palette='coolwarm') # 메모리에 렌더링
plt.show() # 화면에만 출력

# 3.7 seaborn barplot 시각화 실습 문제 : 연도별 승객 수 집계 & 연도별 승객 수를 막대 그래프 출력
# flights = sns.load_dataset('flights')
# print(flights.head(10))
# flights.info()
#
# pvdf = flights.pivot_table(index='year', values='passengers', aggfunc='sum')
# print(pvdf)
#
# sns.barplot(data=pvdf, x='year', y='passengers', palette='coolwarm') # 메모리에 렌더링
# plt.show() # 화면에만 출력

# 3.10 seaborn heatmap() 매트릭스 색상 그래프 / annot,fmt,cbar,cmap 옵션
# heatmap : 데이터의 상관관계를 나타낼 때 많이 쓰임
# flights = sns.load_dataset('flights')
# print(flights.head(10))
#
# flights_pivot = flights.pivot(index='month',columns='year', values='passengers')
# print(flights_pivot)
# plt.figure(figsize=(10,9))
#
# sns.heatmap(flights_pivot, annot=True, fmt='d', linewidths=3, cmap='YlGnBu')
# plt.show()






