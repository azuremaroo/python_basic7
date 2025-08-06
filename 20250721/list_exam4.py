import copy

listdatasrc = [90, [30, 50], 5]
# listdatadest = listdatasrc # 단순 id 복사
# listdatadest = copy.copy(listdatasrc) # listdatasrc 사본 객체를 생성 (리스트 각 항목의 id 만 그대로 복사)
# print(listdatasrc)
# print(id(listdatasrc))
# print(listdatadest)
# print(id(listdatadest))

listdatadest = copy.deepcopy(listdatasrc) # deepcopy() : 리스트 내 리스트가 있는 경우 내부 리스트를 새로 생성하는 함수

listdatasrc[0] = 5
listdatasrc[1][0] = 33

print(listdatasrc) # [5, [33, 50], 5]
print(listdatadest) # [90, [33, 50], 5] src 만 바꿨는데 왜 dest 도 바뀜? ==> 리스트의 항목이 리스트인 경우 id 만 저장하기 때문에

# 결론, 리스트를 복사해서 사본 객체를 생성해야 될 경우 리스트 내부에 리스트가 있는 경우는
# deepcopy() 를  사용해야 하고, 그러지 않은 경우에는 그냥 copy() 를 사용해도 됨