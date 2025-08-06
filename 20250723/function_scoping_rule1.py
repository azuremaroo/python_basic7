
# 함수의 스코핑룰 => 가장먼저 지역공간에 변수를 찾고 없으면 전역공간에 변수를 찾는다!!
# 전역공간에 등록된 변수를 함수를 활용해 변경하는 방법
# 1. return 을 활용
# 2. return 을 활용할 수 없는 환경

def MydataModify():
    # data 변수를 해당 함수에서 사용시 지역공간 새롭게 등록하지말고
    # 전역공간 등록된 변수를 사용해!! => 명령 사용 ==> global 키워드
    global data
    data = 55
    print("함수 내 변수 체크 : ", locals())


data = 90
MydataModify()
print('data : ', data)


a = 3
b = 5
def ReverseData():
    global a, b  # a 변수 와 b변수를 새롭게 등록하지 말고 전역공간에 등록된 변수 사용해!!
    a, b = b, a

print('a : ',a, "  ", 'b : ',b) # 3, 5
ReverseData()
print('a : ',a, "  ", 'b : ',b) # 5, 3


