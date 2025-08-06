

mylistdata = [] # == list() # 리스트 클래스의 객체 생성
print(mylistdata, type(mylistdata), id(mylistdata))
# [] ==> 빈 리스트
# 리스트도 시퀀스 객체 , 색인 연산 가능
# mylistdata[0] = 99 # 인덱스가 없는 리스트에 항목을 추가 할 수 없음!!
# 빈 리스트에 항목을 추가하려면 메서드를 활용해야 함!!
# 항목 추가 메서드 ==> append(), extend(), insert()
mylistdata.append(30)
print(mylistdata)
mylistdata.append("python")
print(mylistdata)
mylistdata.append(59.5)
print(mylistdata)

# 리스트는 항목의 어떤 객체도 저장 가능(올 수 있음)!!
mylistdata.append([5,"study"]) # append() : 리스트의 마지막에 항목을 추가하는 메서드
print(mylistdata)
# 'u' 한 문자만 출력

print(mylistdata[3][1][2])
print("="*80)
print(mylistdata)
mylistdata.extend([80,70]) # extend() : 시퀀스 객체의 항목을 꺼내서 리스트에 넣어주는 메서드
print(mylistdata)

mylistdata.insert(2, [3,4]) # insert() : 특정 위치에 특정 객체를 추가하는 메서드
print(mylistdata)

print("="*80)
print(mylistdata)
print(mylistdata[:3]) # 리스트 슬라이싱 연산
mylist1 = [None]
print(mylist1 * 30) # 리스트 곱셈 연산

mylist2 = [5,6]
mylist3 = ["python", 80]
result = mylist2 + mylist3 # 리스트의 덧셈 연산 ==> 두 리스트를 합쳐줌
print(result)
result[1] = 90
print(result)
