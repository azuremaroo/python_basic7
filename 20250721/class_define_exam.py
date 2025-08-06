
class MyClsData():
    def __init__(self, arg): # 생성자 역할의 함수
        print("객체 생성 완료!!")
        self.data = arg

    def Showdata(self): # 멤버 함수 (메서드)
        print("data : ", self.data)


inst1 = MyClsData(80) # 객체생성
# print(inst1)
# print(inst1.data) # 멤버변수를 외부에서 접근(권장하지 않음)
inst1.Showdata()

inst2 = MyClsData(120) # 객체생성
inst2.Showdata()