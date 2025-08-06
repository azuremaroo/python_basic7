import tkinter
from tkinter import filedialog

mywind = tkinter.Tk()
mywind.geometry("800x600")

sel_fig = 0

def draw_figure(event):
	if sel_fig == 1:
		cvs.create_rectangle(event.x,event.y, event.x+10,event.y+10)
	elif sel_fig == 2:
		cvs.create_oval(event.x-10, event.y-10, event.x+10, event.y+10)
	elif sel_fig == 3:
		cvs.create_line(event.x,event.y,event.x+10,event.y+10)

def draw_rect():
	global sel_fig
	sel_fig = 1

def draw_oval():
	global sel_fig
	sel_fig = 2

def draw_line():
	global sel_fig
	sel_fig = 3

def del_alldraw():
	cvs.delete("all")

def exit():
	mywind.quit()


menubar = tkinter.Menu(mywind)
mywind['menu'] = menubar

menu_draw = tkinter.Menu(menubar, tearoff = 0)
menu_del = tkinter.Menu(menubar, tearoff = 0)
menu_exit = tkinter.Menu(menubar, tearoff = 0)

menubar.add_cascade(menu = menu_draw, label = "도형그리기")
menubar.add_cascade(menu = menu_del, label = "도형 삭제")
menubar.add_cascade(menu = menu_exit, label = "프로그램 종료")

menu_draw.add_command(label = "사각형 그리기", command = draw_rect)
menu_draw.add_command(label = "원 그리기", command = draw_oval)
menu_draw.add_command(label = "선 그리기", command = draw_line)

menu_del.add_command(label = "모두 삭제", command = del_alldraw)

menu_exit.add_command(label = "종료", command = exit)

cvs = tkinter.Canvas(mywind, width = 800, height = 600)
cvs.pack()
cvs.bind("<Button-1>", draw_figure)



mywind.mainloop()