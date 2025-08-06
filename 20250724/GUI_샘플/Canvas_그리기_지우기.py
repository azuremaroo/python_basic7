import tkinter
from tkinter import messagebox

del_sel = 0

def mouseclick(e):
    #print("click posithon", e.x, e.y)
    global m_x, m_y
    m_x, m_y = e.x, e.y

def mousedraw(e):
	global m_x, m_y
	global del_sel
	if del_sel == 0:
		cvs.create_line(m_x, m_y, e.x, e.y)
		m_x , m_y = e.x, e.y
	else:
		cvs.create_line(m_x, m_y, e.x, e.y, fill="white", width = 3)
		m_x , m_y = e.x, e.y

def mymouseup(e):
	global m_x, m_y
	if (m_x,m_y) == (e.x, e.y):
		cvs.create_line(m_x,m_y, m_x+1,m_y+1)

def delete_pic():
	global del_sel
	del_sel = 1

def delete_draw():
	global del_sel
	del_sel = 0


mywin = tkinter.Tk()

frame_up = tkinter.Frame(mywin, width = 500, height = 400)
frame_up.pack()
frame_down = tkinter.Frame(mywin, width = 500, height = 50)
frame_down.pack()

cvs = tkinter.Canvas(frame_up, width = 500, height = 400, bg= "white")
cvs.grid(row=0, column = 0)

button = tkinter.Button(frame_down, text = "그리기", command = delete_draw, foreground = "white", background = "black")
button.grid(row=1, column = 0)

button1 = tkinter.Button(frame_down, text = "삭제하기", command = delete_pic, foreground = "white", background = "black")
button1.grid(row=1, column = 1)

cvs.bind("<ButtonPress-1>", mouseclick)
cvs.bind("<ButtonRelease-1>", mymouseup)
cvs.bind("<B1-Motion>", mousedraw)

mywin.mainloop()
