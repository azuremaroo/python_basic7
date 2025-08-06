def MenuSel():
    print("1.Insert 2.Display 3.Delete 4.Exit")
    sel = int(input("menu sel : "))
    return sel

def InsertData():
    name = input("추가할 이름 : ")
    phonenumber = input("전화번호 : ")
    address_data[name] = phonenumber # 사전에 이름과 전화번호를 저장하는 코드

def DisplayData():
    # print(address_data)
    for name in address_data:
        print(name, " : ", address_data[name])

def DeleteData():
    name = input("삭제할 이름 : ")
    if name in address_data:
        del address_data[name]
    else:
        print("등록되지 않은 이름입니다.")

def run_program():
    while True:
        selmenu = MenuSel()
        if selmenu == 1:
            InsertData() # address_data 라는 빈 사전에 이름과 전화번호 입력 저장
        elif selmenu == 2:
            DisplayData() # 출력
        elif selmenu == 3:
            DeleteData() # 삭제
        elif selmenu == 4:
            print("프로그램 종료")
            break

if __name__ == "__main__": # 해당 파일이 자체 실행 파일일때만 코드가 동작해라!!
    address_data = {} # 빈 사전 객체 생성
    run_program() # 함수 호출