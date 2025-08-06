# tuple 도 시퀀스 객체 (데이터의 순서가 있는)
# 시퀀스 객체의 가장 큰 특징인 색인연산 [index] 지원

mytuple = (30, "python", 6.8) # == tuple()
print(mytuple, type(mytuple))

print( mytuple[1] )
# mytuple[1] = "study" # 값 수정 불가

for x in mytuple:
    print(x, end=" ")


# mytuple = (30) # 튜플 아님 (int 임)
# mytuple = (30,) # 튜플 맞음
# 튜플에 항목이 1개일 때 (30) 으로 쓰면 튜플인지 모르니
# 값 뒤에 콤마(,)를 반드시 추가하여 파이썬에게 "이것은 튜플이다" 알려줘야함

data3 = 3, 4, 5, 6 # tuple 의 pack 기능
data1, data2 = (50, 70) # tuple 의 unpack 기능

print()
print("="*80)
a, b = 6, 7 # pack, unpack 동시
print(a, b)
a, b = b, a # pack, unpack 기능을 통해 swap 가능
print(a, b)

# 파이썬의 함수 동작시 필요사항 ==> 함수 정의, 함수 호출(c는 함수 원형(프로토타입)선언, 호출, 정의 3가지 필요)
# def : 함수 정의 키워드
def MyDataControl(): # 함수 정의
    print("MyDataControl call!!")
    return 50, 70, 90

result1, result2, result3 = MyDataControl() # 함수 호출
# result = MyDataControl() # 반환값을 튜플로 받음
print(result1, result2, result3, type(result1))
