import os

rootdir = 'C:/tempfile_test'  # 현재 작업 디렉토리 경로를 반환 해주는 역할
#print(os.listdir())

with open( os.path.join(rootdir, 'testfile.txt'), 'r+') as f:
    data = f.read()
print(data)