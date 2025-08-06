
dictdata = {"kim":[90,80,70,60], "park":[100,90,65,75], "lee":[88,99,77,66]}
print(dictdata)

# pandas 설치 : 콘솔창 > pip istall pandas ==>
# 콘솔창 > pip list : 설치된 외부 패키지 리스트 확인
# Lib\site-packages 디렉토리에서 설치 확인 가능

import numpy as np # 수치 연산에 특화된 라이브러리
import pandas as pd # 데이터 분석에 특화된 라이브러리

mydf = pd.DataFrame(dictdata) # DataFrame 객체 생성 ==> 2차원 배열 형태의 객체
print(mydf)
print(mydf.columns)

# mydf.to_csv("mydata.csv")
mydf.to_csv("mydata.xlsx")
