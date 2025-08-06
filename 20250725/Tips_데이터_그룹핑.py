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

tipdf = pd.read_csv('tips.csv')
# print(tipdf)
# tipdf.info()
tipdf['tip_rate'] = (tipdf['tip'] / tipdf['total_bill']) * 100 # 팁 비율을 계산해서 새 컬럼 추가
print(tipdf.head(10))
tipdf.info()

# 244 개 데이터 중 tip 비율이 가장 높은 상위 10개 추출
tipdf.sort_values(by=['tip_rate', 'tip'], ascending=False, inplace=True)
print(tipdf.head(10).copy())

# 흡연자/비흡연자 별 tip_rate 의 평균 계산
# 특정 컬럼 키 데이터 기준으로 각각의 데이터를 그룹으로 재구성(형성)하는 기능 ==> 그룹핑
# 그룹핑 연산 지원 메서드 ==> groupby() 연산
# 1. 특정 컬럼 키 기준 데이터를 분할 ( splite )
# 2. 집계통계함수를 특정 컬럼에 적용 ( apply )
# 3. 결과물을 하나의 DataFrame 으로 합쳐줌 ( combine )


# groupby() 연산자의 문법
# tipdf.groupby(그룹핑 기준 컬럼 키)[집계통계함수 적용할 컬럼 선택].agg(적용시킬 집계통계함수를 명시)

# DataFrame 객체를 인덱싱할 때 컬럼을 하나만 선택해도 결과물이 DataFrame 객체로 나오게 하는 방법
# res = grpdf.loc[:, ['a']] # 한 컬럼 데이터를 선택 시 [] 없는 표현은 Series 반환, [] 있는 표현은 DataFrame 반환
# res = grpdf.loc[:, ['a', 'b']] # 연속되지 않은 여러 컬럼 선택
# res = grpdf.loc[:, 'a'] # 'a' 컬럼 선택하여 Series 객체로 반환

grpdf = tipdf.groupby('smoker')[['tip_rate','total_bill', 'tip']].agg('mean') # == .mean(), grpdf 를 DataFrame 의 형태로 받기 위해 [['tip_rate']] 표현 사용
# 그룹핑할 기준 키(컬럼) 데이터는 그룹핑 이후 결과물의 인덱스로 설정
print(grpdf)

print('='*80)

# 요일별 / 흡연자/비흡연자 팁 비율의 평균 계산 출력
grpdf = tipdf.groupby(['day','smoker'])[['tip_rate']].agg('mean')

# print(grpdf)
# print(grpdf.loc[('Sun','No'),['tip_rate']]) # 멀티 인덱스 접근하는 방법 : ('idx1','idx2') 튜플로 접근

unstackdf = grpdf.unstack() # .unstack() : 출력 표 모양 변경
print(unstackdf)
print(unstackdf.columns)
print(unstackdf.loc['Sat', ('tip_rate', 'Yes')]) # 멀티 컬럼즈 접근하는 방법 : ('col1','col2') 튜플로 접근
# 멀티컬럼 자체를 단일 컬럼으로 변환해서 사용하면 더 편함
# 컬럼의 이름을 변경해서 제공

unstackdf.columns = ['tiprate_No', 'tiprate_Yes'] # 멀티 컬럼을 단일 컬럼으로 변경
print(unstackdf)

# unstackdf.plot.bar()
# plt.show()

print('='*80)
print(tipdf)
grpdf = tipdf.groupby(['day', 'gender'])[['tip', 'tip_rate']].agg(['sum', 'min', 'max'])










