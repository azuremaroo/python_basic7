
def EncStringFunc(msg):
    for x in msg:
        #print(x , end=' ')
        if x in EncBook:  # x변수 저장된 문자가 사전에 키로 있냐?
            msg = msg.replace(x,EncBook[x])
    return msg

def DecStringFunc(msg):
    DecBook = {}
    for key in EncBook:
        DecBook[ EncBook[key] ] = key
    #print(DecBook)
    for x in msg:
        # print(x , end=' ')
        if x in DecBook:  # x변수 저장된 문자가 사전에 키로 있냐?
            msg = msg.replace(x, DecBook[x])
    return msg

MyStringData = "I Love Python Programming"
# 사전객체를 활용해서 MyStringData 가 참조하는 문자열을 암호화
EncBook = {'I':'%','P':'*','o':'3','a':'&','m':'8','n':'@', 'r':'6'}
EncString = EncStringFunc(MyStringData)  # 함수호출
print('EncString : ', EncString)  # 암호화된 문자열이 출력

DecString = DecStringFunc(EncString) # 암호화된 문자열을 원 문자열로 복원
print('DecString : ', DecString) # "I Love Python Programming"
