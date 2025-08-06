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

mydf = pd.read_excel("youtube_rank_1000.xlsx")
# print(mydf)
mydf.info() # info() 를 통해 컬럼 데이터 타입과 결측치 유무 확인 필수
print(mydf.head()) # 데이터가 많을 경우 처음부터 5개(기본값)만 출력

del mydf['Subscriber'] # 필요 없는 컬럼 제거
print(mydf.head())

def VideoDataControl(arg): # string 데이터를 머신러닝을 위해 정수형인 int 로 변경
    # return int(arg.replace('개', '').replace(',', '')) # 문자열객체 활용해서 필터링
    return re.sub('[,개]', '', arg) # 정규 표현식 활용해서 필터링

mydf['Video'] = mydf['Video'].apply(VideoDataControl).astype('int64') # Video 컬럼 데이터가 순차적으로 함수에 전달되서 함수에 기능이 적용됨
# mydf['Video'] = mydf['Video'].astype('int64')
mydf.info()

print('='*80)

def view_modify(arg): # 문자열 함수를 이용
    return int(arg.replace('억', '').replace('만', '0000'))

mydf['View'] = mydf['View'].apply(view_modify)

print('='*80)

print(mydf['View'].head(50))
mydf.info()
print(mydf['Category'].unique()) # 특정 컬럼 중복 제거한 리스트
print(len(mydf['Category'].unique()))

# 현재 Category 데이터 중에서 가장 많은 Category 가 뭐냐?
Subset = mydf['Category'].value_counts() # 각 Category 별 개수를 체크해서 Series 객체로 반환
print(Subset)
print()
Subset.info()

Subset_Top5 = Subset[:5].copy()
print(Subset_Top5)

# pie() : 파이 차트 시각화
explode = (0.1, 0.03, 0.03, 0.03, 0.03)
colors = sns.color_palette('pastel')
wedgeprops = {'width': 0.7, 'edgecolor': 'white', 'linewidth': 1}
plt.pie(labels=Subset_Top5.index, x=Subset_Top5,
		autopct="%.2f%%", # 수치 비율 표현
		explode=explode, # 조각 분리
		startangle=90, # 시작 각도
		# pctdistance=0.8, # 라벨을 파이 외곽에 더 가깝게 배치
		counterclock=False, # 시계/반시계 데이터 방향
		colors=colors, # 색상 커마
		shadow=True, # 그림자 효과
		wedgeprops=wedgeprops # 도넛 모양, 데이터 테두리 효과
		)

plt.title('가장 인기있는 유튜브 카테고리', fontdict={'fontweight':'bold', 'fontsize': 16})
plt.show()