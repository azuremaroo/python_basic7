import numpy as np
import pandas as pd

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

tipdf = pd.read_csv('tips.csv')

# groupby 연산과 유사한 동작을 pivot_table() 사용
# values : 집계(통계) 적용할 컬럼 데이터
# index : 그룹핑할 기준키
# aggfunc : 집계 통계할 함수
pvdf = tipdf.pivot_table(index='day', values=['total_bill', 'tip'], aggfunc=['sum', 'mean'], margins=True) # == pd.pivot_table(tipdf, ...) 메서드로 호출할지 함수로 호출할지에 따라 파라미터가 달라짐
# == grpdf = tipdf.groupby('day')[['total_bill', 'tip']].agg(['sum', 'mean'])
print(pvdf)


salesdf = pd.read_excel('salesfunnel.xlsx')
print(salesdf.head())
# salesdf.info()

# pivot_table 메서드 활용하여 다음 결과물을 도출
pvsalesdf = salesdf.pivot_table(index=['Manager', 'Rep', 'Product'],
								values=['Price', 'Quantity'],
								aggfunc=['sum', 'mean'],
								margins=True) # margins=True : 부분합이나 총계를 담기 위한 로우/컬럼 추가 여부
print(pvsalesdf)











