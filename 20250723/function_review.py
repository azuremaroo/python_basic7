
def MyDictControl(**arg):
    print(arg, type(arg))
    print(arg['b'])


MyDictControl(a=5,b=6,c=7,d=8)

#d1, d2 = (1,2)

def Myfunctest(arg):
    total = 0
    for d1, d2 in arg:
        print(d1, d2)
        total += (d1+d2)
    print('total : ', total)


mydata = [ (1,2), (4,5), (8,7)]
Myfunctest(mydata)