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
print(Controldf.head())
Controldf.info()

# 담당 엔지니어와 비고 컬럼 삭제
Controldf.drop(columns=['담당 엔지니어','비고'], inplace=True)
print(Controldf.head())

# Controldf['변경 일자'] = pd.to_datetime(Controldf['변경 일자']) # pd.to_datetime() : 특정 컬럼의 string 데이터를 datetime 으로 변경
# Controldf.info()
#
# Controldf.sort_values(by=['변경 일자'], ascending=False, inplace=True)
# print(Controldf.head(20))
#
# print('='*80)
# Controldf.set_index('변경 일자', inplace=True)
# subset = Controldf.loc['2025-02']
# print(subset)

print('='*80)

def datecut(arg):
	return arg.split('-')[0]
# 1. 변경 일자 데이터를 수정 2025-02-01 ==> 2025

print(Controldf['변경 일자'].apply(datecut))

Controldf['변경 일자'] = Controldf['변경 일자'].apply(datecut)

print('='*80)

# 1. 장비명 중에 숫자문자가 있는 장비명 데이터만 추출
def DeviceNameFind(arg):
	return len(re.findall('[0-9]+', arg)) > 0

print(Controldf.loc[Controldf['장비명'].apply(DeviceNameFind)])
# == print(Controldf.loc[Controldf['장비명'].str.contains('[0-9]'), :])


