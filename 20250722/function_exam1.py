

# 함수 정의
def ListDataSum(arg, start=0): # start=0 : 디폴트 파라미터 ==> 전달인자값이 없을 경우 디폴트로 설정된 값으로 코드 수행
    print("arg : ", arg)
    total = 0
    for x in arg[start:]:
        total += x
    print("total : ", total)

# 함수 호출
ListDataSum([5,6,7,8,9,10], 5)

def tupleDatasum(*arg): # *arg : 가변 인수를 tuple 로 받는 파라미터
    # print(arg, type(arg))
    total = 0
    for x in arg:
        total += x
    print("total : ", total)

tupleDatasum(3,4,5,6,7,8,9) # 가변 인수
tupleDatasum(3,4,5) # 가변 인수

def SumofList(arg1, arg2):
    # print(arg1, arg2)
    result = []
    for idx, item  in enumerate(arg1):
        result.append(item + arg2[idx])
    return result, len(result) # 여러개 리턴 가능(튜플 타입)

result = SumofList([5,6,7,8], [4,5,2,7]) # 함수 리턴값이 없을 경우 기본적으로 None 객체를 반환
print("result : ", result) # [9, 11, 9, 15]
