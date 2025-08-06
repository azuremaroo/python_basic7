
class SumofDataCls():
    def __init__(self, *arg):
        self.mdata = arg

    def ShowData(self):
        print(self.mdata)
        print("총합 : ", sum(self.mdata) )
        print("평균 : " , sum(self.mdata) / len(self.mdata))

myobj = SumofDataCls(5,6,7,8,9,10)
myobj.ShowData()  #  총합 과 평균 출력