# 시퀀스 객체 ==> 문자열, 리스트, 튜플

# 매핑 타입 객체 ==> dict 타입 ( 데이터의 순서가 없는 타입, 색인 연산 X )
# 매핑 ==> 특정 key 와 특정 value 를 매핑해 놓은 형태 ( key : value )
mydict = {'A' : 50, 'B' : 80, 'C' : 90}  # {} == dict()
print(mydict, type(mydict))
print(mydict['A']) # A 키 값에 대한 Value 값을 반환해라
print(mydict['C'])

# 새로운 데이터를 사전에 추가
mydict['K'] = 77 # 'K' 에 대한 77 Value 를 사전에 추가해라!!

# 기존 키가 있는 상태에서 데이터를 추가
mydict['B'] = 33 # 기존 key 에 대한 value 를 업데이트 시키는 문법!!
print(mydict)

# 항목 삭제
del mydict['C']
print(mydict) # {'A': 50, 'B': 33, 'K': 77}


for key in mydict: # 반복문에 사전이 올 경우 변수에 key 만 전달
    print(key, " : ", mydict[key])

print ('m' in mydict) # 'K' 키값이 사전에 키로 있냐?