import numpy as np
# num1 = 5
#
# mylist = [ num1, "python", [20,30], 9.8 ]
#
# print(mylist)
#
# print(id(num1))
# print(id(mylist[0]))
#
# mylist[0] = 6
# print(mylist)
#
# print(id(num1))
# print(id(mylist[0]))


mylist = [ 5, "python", [20,30], 9.8 ]

print(mylist)
print(mylist[1].replace('y', 'k'))
mylist[2].append(79)
print(mylist[2])
mylist.append("test")
print(mylist)
print(mylist[1:3]) # 슬라이싱 연산

mylist1 = [5,6,7,8]
mylist2 = [3,4,5,6]
print(mylist1 + mylist2)

arr1 = np.array(mylist1) + np.array(mylist2) # numpy 배열로 변환
print(arr1)
print(arr1, type(arr1), arr1.ndim, arr1.shape) # .ndim, .shape
# arr2 = np.arange(1,10,2)
arr2 = np.arange(0,12).reshape(3,4)
# print(arr2, len(arr2))
print(arr2.shape, arr2.ndim) # .shape : numpy 배열의 모양, .ndim : 배열의 차원 수
print(arr2)
print(arr2[0:2,0:2]) # 2 차원 배열 슬라이싱

# 파이썬 기본 범위 데이터 생성 클래스
print( list( range(0,12) ) )
for x in range(3, 15): # range() : 반복문의 횟수 역할
    print(x, end = ' ')
print()

mydata1 = list(range(1,66))
print(mydata1)

mylistdata1 = [3, [5,6], 80, 90]
for index, item in enumerate(mylistdata1): # enumerate() : 인덱스와 항목을 동시에 반환
    print(index, item)

