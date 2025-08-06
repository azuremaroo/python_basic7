# 문자열 객체의 특징
# 시퀀스 객체 ==> 데이터의 순서가 있는 객체(문자열, 리스트, 튜플)

data1 = "python programming"
# [0] ==> 표기법을 이용해서 객체의 항목에 접근 ==> 색인연산
# 색인 연산이 가능한 객체는 시퀀스 객체만 가능
print(data1[0])
print(data1)
print(data1[5])

# 문자열 객체의 + 연산 ==> 두 문자열을 합친 문자열 생성
data2 = "study"
print(data1 + ' ' + data2)

# 문자열 객체의 * 연산 (곱셈 연산) ==> 문자열을 n 만큼 반복한 문자열 생성
print('=' * 50)
print(data1[-1]) # 색인연산의 마지막 항목(-1)을 반환
print(len(data1)) # len() : 객체의 길이를 반환하는 함수

data3 = "programming Good"
print(data3)
print(id(data3))
#data3[0] = 'P'
print(data3) # TypeError: 'str' object does not support item assignment 오류(문자열 객체는 아이템 할당을 지원하지 않음)
# 문자열 객체는 해당 항목을 수정할 수 없는 객체
data4 = data3.capitalize() # 문자열의 첫 문자만 대문자로 변경한 문자열을 생성하는 함수
print(data4)
print(id(data4))
print('=' * 80)
print(data3)
#시퀀스 객체에 사용되는 슬라이싱(slicing) 연산
#data3[start:stop] # start ~ stop-1 까지 수치데이터로 전달해서 잘라내라!!
print(data3[0:11])
print(data3[:11]) # 0은 생략 가능
print(data3[12:]) # stop 을 생략할 경우 끝까지를 의미
print("data3[::2] " + data3[::2]) # start : stop : step 시작부터 끝까지 2씩 건너뛰어라

#data3[:] 모든 내용을 참조해라
print(data3[::1]) # start : stop : step
print(data3[::-1]) # start : stop : step

# 문자열 중에 어떤 내용이 있는지 체크 할 때 사용하는 문법
print('ko' in 'programming')

# 시퀀스 객체에 반복문을 사용할 경우 한 항목씩 변수에 전달!!
# for 변수 in 시퀀스객체 :
#     수행구문
count = 0
for item in 'python programing good':
    print(item, end=' ')
    if item == 'g':
        count = count + 1

print()
print("count : ", count)


