import numpy as np
import pandas as pd

#index_col=0 : 엑셀의 첫번째 컬럼을 인덱스로 설정해서 DataFrame 생성
StScoredf = pd.read_excel("StudentScore.xlsx", index_col=0) # 엑셀파일을 읽어와서 DataFrame 객체로 생성
print(StScoredf)

# 특정 행과 열 데이터 삭제 메서드 ==> drop()
# 특정 컬럼 삭제 ==> del 키워드 활용
# print('='*50)
# del StScoredf['SubjectMean']
# print(StScoredf)

# 특정 행을 삭제 ==> drop()
# axis = 0 (행축), axis = 1 (열축)
# 행축으로 움직이면서 라벨이 StudentMean 인 행을 삭제해라!!
# inplace = True : 사본 객체를 생성하지 말고 원본 객체에 직접 반영해!! (반환할 사본이 없으므로 반환값 None 객체)
# inplace = False : 특정 행이 삭제된 사본 객체를 생성해서 반환해
print('='*50)
# subDF = StScoredf.drop(['StudentMean'], axis=0, inplace=False)
subDF = StScoredf.drop(['kor','StudentMean'], axis=0, inplace=False)
subDF = StScoredf.drop(['lee','SubjectMean'], axis=1, inplace=False)
print(subDF)
