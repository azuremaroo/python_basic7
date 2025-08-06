import numpy as np # as : 엘리어싱(별칭)


mylist = [5, 6, 8, 3]
print(mylist)

arr1 = np.array(mylist) # 리스트를 numpy 배열로 다시 생성
print(arr1 + 2) # [2, 2, 2, 2] 로 브로드캐스팅 후 연산

print(mylist[2])
# del 키워드 활용 ==> 항목 삭제
del mylist[2]
print(mylist)

mylist3 = [ 7, 3, 2, 8, 6, 1 ]
# 현재 리스트 항목을 오름차순으로 정렬?
# 리스트 메서드를 활용한 정렬
# mylist3.sort() # sort() : 리스트의 정렬 메서드는 자기 자신을 정렬시키고 사본객체를 반환하지 않음
# print(mylist3)

# mylist3.sort(reverse=True)
# print(mylist3)

mylist4 = sorted(mylist3) # 파이썬 내부 정렬 함수
print(mylist4) # 정렬된 사본 객체를 반환
print(mylist3)
