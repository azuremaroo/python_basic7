# 사진기능
# 전화기능
# display 기능 등 다양한 기능을 종합적으로 동작시키는 main 파일

# 파일명이 모듈명이 됨!!
import phonecall_operation as pho
import picture_operation as pic

if __name__ == "__main__":
    print("__name__ : ", __name__) # 파이썬 내부 특수 역할 변수
    pho.phonecall_func()
    pic.picture_func()
# __name__ : 특수 변수로 현재 파일이 실행 모듈일 경우 __main__ 값을 갖음!!
# __name__ : 특수 변수는 import 일 경우에는 모듈명을 갖음!!
