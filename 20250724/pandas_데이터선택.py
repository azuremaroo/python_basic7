import numpy as np
import pandas as pd

#index_col=0 : 엑셀의 첫번째 컬럼을 인덱스로 설정해서 DataFrame 생성
StScoredf = pd.read_excel("StudentScore.xlsx", index_col=0) # 엑셀파일을 읽어와서 DataFrame 객체로 생성
print(StScoredf)

del StScoredf['SubjectMean']
StScoredf.drop(['StudentMean'], axis=0, inplace=True)
print(StScoredf)

# 슬라이싱 연산을 활용한 특정 데이터 추출
# 라벨 인덱싱의 경우 Stop 을 포함!!
# subset = StScoredf.loc['kor':'math', 'kim':'park']
# print(subset)

# 정수 인덱싱을 활용한 추출 ==> iloc
# 정수 인덱싱인 경우 Stop-1 까지 포함
# print('='*50)
# subset = StScoredf.iloc[0:2, 0:2]
# print(subset)
#
# print('='*50)
# subset = StScoredf.loc['math':'eng', 'park':'lee']
# subset = StScoredf.iloc[1:3, 1:3]
# print(subset)

# 'kim' 학생 기준으로 점수가 60점 초과인 항목만 추출
print(StScoredf['kim'] > 60) # 각 항목별 비교 연산에 대한 결과가 반환 ==> 불린배열 생성

# 불린배열을 활용한 불린색인
subset = StScoredf.loc[StScoredf['kim'] > 60, 'kim':'park']  # ==> 불린배열의 True 인 항목만 추출
print(subset)


