import numpy as np
import pandas as pd

# === pnadas 출력 제어 옵션 설정 시작 ===
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
# === pnadas 출력 제어 옵션 설정 끝 ===

tipdf = pd.read_csv("tips.csv")
# print(tipdf)
tipdf.info() # 정보 확인
print('='*80)
print(tipdf.head()) # head(): DataFrame 머리(처음) 부터 (5)행만 선택해서 출력
print('='*80)
print(tipdf.tail()) # tail(): DataFrame 꼬리(뒤) 부터 (5)행만 선택해서 출력
print('='*80)
print(tipdf.sample(5)) # sample(num): DataFrame 랜덤하게 (num)행만 선택해서 출력
print('='*80)
print(tipdf['day'].unique()) # 컬럼데이터의 유일한 항목을 추출해서 표현
print(tipdf['time'].unique())
print(tipdf['gender'].unique())

# 특정 컬럼 데이터를 일괄 map OR 함수 적용해서 데이터를 변경하는 기능 ==> 함수 적용
print('='*80)
tipdf['gender'] = tipdf['gender'].map({'Female':1, 'Male':0})
print(tipdf.sample(5))
print(tipdf.info())


print('='*80)
tipdf_head10 = tipdf.head(10).copy() # .copy() : 원본의 view 객체가 아닌 완벽한 사본 객체 생성
print(tipdf_head10)

print('='*80)
def tipdata_increase(arg):
    # print('arg : ', arg)
    return arg + 2

# 함수적용 기능 :
# apply() 이용해서 특정 컬럼 데이터를 일괄 함수 적용해서 데이터 변형하는 동작
tipdf_head10['tip'] = tipdf_head10['tip'].apply(tipdata_increase) # .apply(func) : func 각 항목 데이터에 적용시킬 함수명
print(tipdf_head10)