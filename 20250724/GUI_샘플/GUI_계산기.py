import tkinter

root = tkinter.Tk()
root.title("4칙 계산기")

root.resizable(0,0)

# 연산식 표현 변수 선언
oper_exp = ""
result = tkinter.StringVar()

cal_Label = tkinter.Label(root, textvariable=result)
result.set("계산식을 입력하세요 : ")
cal_Label.grid(row=2, columnspan=8)

def NumButton(num):
    global oper_exp
    oper_exp = oper_exp + str(num)
    result.set(oper_exp)

def EqualButton():  # 12+3
    global oper_exp
    total = str(eval(oper_exp))
    result.set(total)
    oper_exp = ""

def ClearButton():
    global oper_exp
    oper_exp = ""
    result.set("")


Button0 = tkinter.Button(root, text="0", bg='white',command=lambda: NumButton(0), height=1, width=7, borderwidth=3)
Button0.grid(row=6, column=2, padx=10, pady=10)
Button1 = tkinter.Button(root, text="1", bg='white',command=lambda: NumButton(1), height=1, width=7, borderwidth=3)
Button1.grid(row=3, column=1, padx=10, pady=10)
Button2 = tkinter.Button(root, text="2", bg='white',command=lambda: NumButton(2), height=1, width=7, borderwidth=3)
Button2.grid(row=3, column=2, padx=10, pady=10)
Button3 = tkinter.Button(root, text="3", bg='white',command=lambda: NumButton(3), height=1, width=7, borderwidth=3)
Button3.grid(row=3, column=3, padx=10, pady=10)
Button4 = tkinter.Button(root, text="4", bg='white',command=lambda: NumButton(4), height=1, width=7, borderwidth=3)
Button4.grid(row=4, column=1, padx=10, pady=10)
Button5 = tkinter.Button(root, text="5", bg='white',command=lambda: NumButton(5), height=1, width=7, borderwidth=3)
Button5.grid(row=4, column=2, padx=10, pady=10)
Button6 = tkinter.Button(root, text="6", bg='white',command=lambda: NumButton(6), height=1, width=7, borderwidth=3)
Button6.grid(row=4, column=3, padx=10, pady=10)
Button7 = tkinter.Button(root, text="7", bg='white',command=lambda: NumButton(7), height=1, width=7, borderwidth=3)
Button7.grid(row=5, column=1, padx=10, pady=10)
Button8 = tkinter.Button(root, text="8", bg='white',command=lambda: NumButton(8), height=1, width=7, borderwidth=3)
Button8.grid(row=5, column=2, padx=10, pady=10)
Button9 = tkinter.Button(root, text="9", bg='white',command=lambda: NumButton(9), height=1, width=7, borderwidth=3)
Button9.grid(row=5, column=3, padx=10, pady=10)

Cal_Add = tkinter.Button(root, text="+", bg='white',command=lambda: NumButton("+"), height=1, width=7, borderwidth=3)
Cal_Add.grid(row=3, column=4, padx=10, pady=10)

Cal_sub = tkinter.Button(root, text="-", bg='white',command=lambda: NumButton("-"), height=1, width=7, borderwidth=3)
Cal_sub.grid(row=4, column=4, padx=10, pady=10)

Cal_Mul = tkinter.Button(root, text="*", bg='white',command=lambda: NumButton("*"), height=1, width=7, borderwidth=3)
Cal_Mul.grid(row=5, column=4, padx=10, pady=10)

Cal_Div = tkinter.Button(root, text="/", bg='white',command=lambda: NumButton("/"), height=1, width=7, borderwidth=3)
Cal_Div.grid(row=6, column=4, padx=10, pady=10)

Equal = tkinter.Button(root, text="=", bg='white',command=EqualButton, height=1, width=7, borderwidth=3)
Equal.grid(row=6, column=3, padx=10, pady=10)

Clear = tkinter.Button(root, text="C", bg='white',command=ClearButton, height=1, width=7, borderwidth=3)
Clear.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()