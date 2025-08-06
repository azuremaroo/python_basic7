print("data type")
# 파이썬 ==> OOP 객체 지향 언어
# 객체 지향 언어의 특징 ==> 1. 캡슐화(클래스) 2. 상속 3. 다형성

# 문자열 객체
# 문자열 객체 생성시 ==> " ", ' ' 선언하면 str 클래스를 활용해 객체 생성
# s1 = str() # str 클래스를 활용해서 객체를 생성
# s1 = '' # == str(), str 클래스를 활용해서 객체를 생성
s1 = "python programming" # == str(), str 클래스를 활용해서 객체를 생성
print(id(s1)) # id() : 해당 객체의 id 를 반환하는 함수
print(type(s1)) # type() : 해당 객체의 클래스 타입을 반환하는 함수

s2 = "Good Study"
print(id(s2)) # id() : 해당 객체의 id 를 반환하는 함수
print(type(s2)) # type() : 해당 객체의 클래스 타입을 반환하는 함수

s3 = 50
print(id(s3)) # id() : 해당 객체의 id 를 반환하는 함수
print(type(s3)) # type() : 해당 객체의 클래스 타입을 반환하는 함수

# 파이썬의 변수 역할 : 객체의 id 를 저장해서 참조하는 역할(그래서 타입이 달라도 담을 수 있음)

s4 = 7.9
print(id(s4)) # id() : 해당 객체의 id 를 반환하는 함수
print(type(s4)) # type() : 해당 객체의 클래스 타입을 반환하는 함수

s5 = True
print(id(s5)) # id() : 해당 객체의 id 를 반환하는 함수
print(type(s5)) # type() : 해당 객체의 클래스 타입을 반환하는 함수

# "", '' 문자열 객체 생성 방법
print("I'm python!!") # 문자열에 작은 따옴표가 있을 때 큰 따옴표 사용(반대도 마찬가지)
print() # 줄바꿈(개행, end 파라미터에 디폴트값이 '\n' 이므로)
print("test programming") # print() : 전달된 문자열을 화면에 출력하는 역할의 함수
