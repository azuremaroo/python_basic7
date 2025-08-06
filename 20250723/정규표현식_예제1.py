#
# 특정패턴을 활용해서 문자열 중 특정 문자열을 찾고(검색), 삭제, 필터링 하는 문법으로 사용
import re # 정규표현식 모듈 추가

stringdata = "파두, FmS 2025서 메타와 ㅎㅎ 기조연설…AI 1998데이터센터용#ssd 비전 3제시 ks k"

# 특정 패턴을 활용해서  문자열의 특정 문자열을 찾는 메서드 ==> 결과를 리스트로 반환
#re.findall(패턴, 원본문자열)
# 문자열 중 숫자 문자를 찾아서 반환?
# '[0-9]' : 숫자 문자 개별 패턴
# + (메타문자)  ==> + 기호앞에 있는 패턴은 하나이상의 패턴을 의미
# '[0-9]+' ==> 숫자문자가 하나 이상인 패턴
result = re.findall('[0-9]+', stringdata)
print(result)

# 영문대문자가 하나 이상인 문자열을 찾아서 반환?
result = re.findall('[A-Z]+', stringdata)
print(result)

# 영문소문자가 하나 이상인 문자열을 찾아서 반환?
result = re.findall('[a-z]+', stringdata)
print(result)

# 영문대소문자가 하나 이상인 문자열을 찾아서 반환?
result = re.findall('[a-zA-Z]+', stringdata)
print(result)

# 한글 조합형부터 완성형 까지 모든 한글 문자열 찾는 패턴 : [ㄱ-힣]+
# 한글 완성형 패턴 ==> '[가-힣]+'
result = re.findall('[가-힣]+', stringdata)
print(result)

# * : 이 메타문자 앞의 패턴이 0개 이상인 패턴을 찾아라
result = re.findall('ks+', stringdata)
print(result)


mail_address = '홍길동 이메일 주소는 Hong_gilldong@naver.com 입니다'
result = re.findall('[a-zA-Z]+[_.a-zA-Z0-9]+@[a-z]+[.][a-z]+[.]*[a-z]*',mail_address)
print(result)

str1 = 'te#st pyth!on,good st%udy'

result = re.sub('[#!%]','',str1)  # == replace() 효과
print(result) # test python,good study
# \s : 공백문자
result = re.split('[\s,]',result)
print(result)