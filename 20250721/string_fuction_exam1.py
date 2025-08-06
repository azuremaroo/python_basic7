#
# str1 = "test"
#
# print("이름 : {}, 나이 : {}, 몸무게 : {}".format("Hong", 50, 68.9))
#
# print("데이터 : {0:.3f} ".format(3.145678))
#
# print(" menu ".center(50, "*"))
#
# mylist = ['python', 'study', 'good', 'test']
#
# # 여러개의 문자열 객체를 하나의 문자열 객체로 합쳐주는 메서드
# result = ", ".join(mylist)
# print(result)

with open("stringdata.txt", 'r+') as f:
    # mystr = f.read() # 현재 파일의 내용을 모두(전체) 읽어와서 하나의 문자열 객체로 생성
    # mystr = f.readline() # 현재 파일의 첫번째 줄만 읽어 들임
    mystr = f.readlines() # 라인별로 읽어서 리스트의 항목으로 반환

#with as 구문 이 벗어나면 자동 파일 객체 close() 동작함
print(mystr) # 리스트 클래스의 객체
print(type(mystr))

# 현재 mystr 객체의 항목을 깨끗한 문자열 객체로 생성해서 합치자!!
# print(mystr[1].strip()) # strip() : 앞뒤 공백, 개행 모두 제거

datalist = []
for item in mystr:
    print(item.strip(), end=" ")
    datalist.append(item.strip())

print()
print(datalist)
result = ",".join(datalist)
print(result)

# import re # 정교표현식 문법
mystrdata1 = "python,programming/study#good"
result = mystrdata1.split(",") # 구분자를 이용해서 문자열을 분할한다음 리스트로 반환해라!!
print(result)
# result = re.split('[,/#]', mystrdata1)
# print(result)

mystrdata2 = "time is gold"
mystrdata2 = mystrdata2.replace('gold', 'apple') # gold 를 apple 로 바꾼 새로운 문자열 객체 생성
print(mystrdata2)
print(mystrdata3)
