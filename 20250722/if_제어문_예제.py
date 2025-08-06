# 제어문 ==> 단독 if, if~else, if~elif

a = 6
b = 8
if a > b :
    print("a 가 더 큼")
else:
    print("a 가 더 작음")
    
# 경우가 여러가지 존재할 경우
# if 조건:
#     pass
# elif 조건:
#     pass
# elif 조건:
#     pass
# else:
#     pass

# a = 5
# b = 7
# max = 0
# if a > b:
#     max = a
# else:
#     max = b

# 간단한 if~else 구문을 한 라인으로 표현 ==> 조건 표현식 문법
# max = (a > b) ? a : b # c의 삼항연산자
max = a if a > b else b # 조건표현식
print("max : ", max)

# 리스트 내포 문법
# listdata = []
# for x in range(1,10):
#     listdata.append(x) 3 줄을 아래 한줄로 표현
listdata = [ str(x) for x in range(1,10) ] # range(1,10) 1부터 9까지 범위데이터 생성
print("".join(listdata)) # 리스트 생성과 동시에 타입 변환도 가능

listdata2 = [ x for x in range(0,100) if x%2 == 0 ] # 여과기 동작(else 사용 불가)
print(listdata2)

listdata3 = [ str(x) if x % 2 == 0 else ' ' for x in range(5, 15) if not x == 10 ] #  타입 변환 + 조건 표현식 + 리스트 내포 + 여과기
print(listdata3)