import numpy as np
import pandas as pd

scoredf = pd.DataFrame( {"kim": [60,90,80], "park": [80,77,99], "lee": [66,89,79]},
                        index=['kor', 'math', 'eng'] )
print(scoredf) # 사전의 키를 DataFrame 컬럼 인덱스로 자동 설정
print('='*50)

# 한 컬럼 선택 문법 ==> DataFrame 객체
onedata = scoredf['park']
print(onedata) # 'park' 한 컬럼 데이터를 추출 하는 문법
print(type(onedata)) # DataFrame 의 한 컬럼 데이터 선택은 Series 객체이다!!

# 새로운 컬럼 데이터 추가 문법
print('='*50)
scoredf['song'] = 90 # 50 이 브로드캐스팅돼서 입력됨, [50,70,80]
print(scoredf)

# 새로운 행 데이터 추가 문법 => Loc 인덱스를 사용!!
print('='*50)
scoredf.loc['music'] = [55,66,77,88]
# scoredf.loc['music'] = 55
print(scoredf)

# SubjectTotal 컬럼, avg 행 추가
print('='*50)
scoredf['SubjectMean'] = np.nan # np.nan : 결측치(NaN) 데이터 표현(엑셀의 공란)
scoredf.loc['StudentMean'] = np.nan
print(scoredf)

# scoredf.to_excel("StudentScore.xlsx")

# sum(), mean(), max(), min() ==> 집계통계 함수 지원
print('='*50)
print(scoredf['kim'].mean()) # 한 사람 평균
print(scoredf.loc['kor'].mean()) # 한 과목 평균
print(scoredf)

# 4 학생의 평균을 빈 리스트에 저장해서 출력
print('='*50)
# studentmeans = [ float(scoredf[col].mean()) for col in scoredf.columns ]
# print(studentmeans) # 학생 평균
# subjectmeans = [float(scoredf.loc[idx].mean()) for idx in scoredf.index]
# print(subjectmeans) # 과목 평균

scoredf['SubjectMean'] = [float(scoredf.loc[idx].mean()) for idx in scoredf.index]
scoredf.loc['StudentMean'] = [ float(scoredf[col].mean()) for col in scoredf.columns ]
print(scoredf)

scoredf.to_excel("StudentScore.xlsx") # 엑셀로 저장
