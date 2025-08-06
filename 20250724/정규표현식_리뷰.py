

import re # 정규표현식 모듈 패키지
# 정규표현식 활용 ==> 특정패턴을 이용해서 문자열 데이터 중 특정 문자열을 찾고(검색), 삭제(치환), 분리(분할) 하는 기능으로 사용해라!!


stringdata = "파이썬 1998 프로그래밍,Study Good!!"

# 검색(특정 문자열을 리스트로)
result = re.findall('[가-힣a-zA-Z0-9]+', stringdata)
print(result, type(result))

result = re.findall('[^\s,!]+', stringdata) # ^\s,! ==> \s,! 이 아닌 패턴을 찾아라
print(result, type(result)) # ['파이썬', '1998', '프로그래밍', 'Study', 'Good'] <class 'list'>

# 분할
result = re.split('[#,\s]', stringdata)
print(result, type(result))


# 특정 문자열 치환
# str1 = "235,512개"
# result = int(re.sub('[,개]', '',str1))
# print(result + 15, type(result))