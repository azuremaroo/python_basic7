

# 클래스 설계 ( 사용자가 직접 정의 )
# 클래스 정의 키워드 ==> class

class MyClsData():  # 클래스 정의
    def __init__(self, arg):
        print("객체 생성 완료!!")
        #listdata = arg   # 해당 함수 내에서만 접근이 가능한 지역 등록 변수
        self.listdata = arg  # 객체의 멤버변수로 등록되고 초기화

    def ShowData(self):
        print("출력 : ", self.listdata)  # 멤버함수(메서드)를 활용해서 멤버 변수를 접근 출력

# 객체가 생성될때 자동으로 호출 되는 특수한 함수  ==> 생성자 함수
# __init__()
inst = MyClsData([5,6,7,8,9]) # MyClsData 클래스를 바탕으로 객체를 생성해라!
#print(inst.listdata)  # 객체의 멤버 변수를 외부에서 접근 출력
inst.ShowData()


inst2 = MyClsData([13,16,17,18,19]) # MyClsData 클래스를 바탕으로 객체를 생성해라!
inst2.ShowData()

