#
# #input() : 기본적으로 입력 객체를 문자열 객체로 생성!!
# data1 = int( input("정수 데이터 하나 입력 : ") ) # c 언어의 printf + scanf 동작과 유사
# data2 = int( input("정수 데이터 하나 입력 : ") ) # 문자열 객체를 정수객체로 타입변환
#
# print(data1 + data2)


saved_pw = 'python'
while True: # 무한 반복 구문
    input_str = input("password 입력( 종료 : quit) ==> ") # 들여쓰기로 실행문의 코드블록 구별
    if input_str == saved_pw:
        print('pw success!!')
    elif input_str == 'quit':
        break # 반복문 탈출
    else:
        print('pw fail!!')
