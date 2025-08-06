import numpy as np
import pandas as pd

# range() 파이썬 기본 수치 범위 데이터 생성
# np.arange() 넘파이 수치 범위 배열 데이터 생성

# pandas 의 시간 범위 데이터를 생성하는 메서드
dateidx = pd.date_range('2024.12.25',
              periods=50, # 기간
              freq='D') # 주기(월, 일, 시, 분), 'D' => day, 'ME' => month, 'h' => hour
print(dateidx) # 시계열 데이터 : dtype='datetime'

arr1 = np.arange(1, 101).reshape(50,2)
print(arr1)

mydf = pd.DataFrame(arr1, index=dateidx, columns=['A','B'])
print(mydf)
# mydf.info()

print('='*80)

# 시계열 데이터의 장점 ==> '2025/02', '2025-02', '2025.02' 모두 2024년 2월 데이터를 선택 추출
print( mydf.loc['2025/02/01':'2025/03/01'] ) # 범위 추출

pricedf = pd.read_csv('price_data.csv')
print(pricedf)
pricedf.info() # RangeIndex: 10 entries, 0 to 9

# to_datetime() : 문자열 형태의 시간 데이터를 시계열 데이터(datetime) 타입으로 변경해주는 메서드
pricedf['날짜'] = pd.to_datetime(pricedf['날짜'])
# print(pricedf)

# pricedf.reset_index() # 인덱스 초기화
pricedf.set_index('날짜', inplace=True)
print(pricedf)
pricedf.info() # Index: 10 entries, 2020.04.02 to 2020.03.20

print(pricedf.loc['2020-04']) #