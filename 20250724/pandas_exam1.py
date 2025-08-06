import numpy as np
import pandas as pd
import random

# random : 임의의 데이터를 생성할 때
# randint() ==> 해당 범위 내에서 임의의 정수 데이터를 추출
# 그리고 해당 shoape 형태로 추출해서 구성
arr1 = np.random.randint(1,46, (5,6)) # numpy 로또 번호 생성기(1~45 번호를 랜덤으로 뽑아서 5,6 의 2차원 배열로)
print(arr1, type(arr1)) # numpy 배열

# data = random.randint(1,46) # 파이썬 기본 random 함수는 한번에 하나만 뽑기 가능
# print(data)

# numpy 배열은 특정 항목 데이터를 접근할때 수치 index 로만 접근이 가능
print(arr1[0,2]) # 특정 데이터는 arr1[행접근,열접근] 사용 (arr1[행][열] 은 사용 x)
print(arr1[:3, :2]) # 범위는 arr1[행슬라이싱,열슬라이싱] 사용

arr2 = np.arange(1, 31).reshape(5,6)
print(arr2)

# pandas ==> 1차원 배열 형태의 Series 객체, 2 차원 배열 형태의 DataFrame 객체를 지원
# pandas의 객체는 numpy배열(수치만 지원)과 달리 컬럼과 인덱스의 라벨(문자열) index 까지 지원함
mydf = pd.DataFrame(arr2, columns=list("abcdef"), index=['one','two','three','four','five']) # numpy 배열로 DataFrame 객체를 생성해라!!
print(mydf, type(mydf))
# print(mydf.columns)
# print(mydf.index)

# 특정 데이터 접근
# 현재 명시적 인덱스인 라벨 인덱스로 접근할 경우 ==> Loc 인덱서(Label Location)
print(mydf.loc['four','b'])
#암묵적인 인덱스(수치) 인덱스로 접근할 경우 ==> iloc 인덱스(Integer Location)
print(mydf.iloc[3,1])
# print(mydf['b']['four']) # mydf['b'] ==> Series 객체(1차원 배열)로 접근(DataFrame 에 접근할 때 이 방법은 좋지 않음)