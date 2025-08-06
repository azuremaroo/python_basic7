
# open() : 디스크에 저장된 파일을 접근해서 파일 객체로 생성해주는 함수
# 경로를 포함한 파일 ,  해당 파일의 접근 모드 를 설정
# 'r+' : 읽고 쓰는 모드
# f = open('testfile.txt', 'r+')
# mystr = f.read()  # 해당 파일의 모든 내용을 읽어와서 하나의 문자열 객체로 생성
# print(mystr)
# print( f.tell() ) # 현재 파일포인터 위치를  출력
# f.seek(0,0) # 현재 파일포인터 위치를 맨 앞으로 이동
# print( f.tell() )
# #mydata = f.read()
# #print(mydata)
# f.write("C test")
# f.close()

# 'w' : 해당 파일이 없으면 새로운 파일을 생성
#  해당 파일이 있으면 해당 파일에 새로운 내용을 덮어씀.
# f = open("codetest.txt",'w')
# f.write("C/C++ prorammig")
#
# f.close()
#

# with ~ as 문법
with open('testfile.txt', 'r+') as f:
    readdata = f.read()

print(readdata)

