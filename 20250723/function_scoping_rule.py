
# 함수의 스코핑룰 => 가장먼저 지역공간에 변수를 찾고 없으면 전역공간에 변수를 찾는다!!
def MydataModify():
    #data -= 35  # data = data - 35
    data = 55  # 함수 내에서만 접근이 가능한 지역공간에 변수
    # 해당지역에 등록된 변수가 어떤게 있는지 체크하는 함수 => locals() : 사전형태로 반환
    print("함수내 변수 체크 : ", locals()) #  {'data': 55}
    print('함수 내 data 출력 : ', data)


data = 90
print('data : ', data) # 90
MydataModify()
print("함수 밖(전역공간) 의 변수 체크 : ", locals())
print('data : ', data)