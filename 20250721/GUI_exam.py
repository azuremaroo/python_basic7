import tkinter as TK # GUI 지원 라이브러리(패키지)

def button1_oper():
    print("b1 oper!!")

mywind = TK.Tk() # main 윈도우 객체 생성
mywind.geometry("600x600")
b1 = TK.Button(text = "button test", padx= 30, pady=30, bg="blue", command=button1_oper)
b1.pack() # 배치
mywind.mainloop()