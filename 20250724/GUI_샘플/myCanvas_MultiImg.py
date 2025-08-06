import tkinter
import time
mywin = tkinter.Tk()
cvs = tkinter.Canvas(mywin, width=600, height = 400, bg="white")
cvs.pack()
x = 300
y = 200
fmimg1 = tkinter.PhotoImage(file = "Flashman1.png")
fmimg2 = tkinter.PhotoImage(file = "Flashman2.png")
fmimg3 = tkinter.PhotoImage(file = "Flashman3.png")

Img_list = [fmimg1, fmimg2, fmimg3]

for img in Img_list:
	cvs.create_image(x,y, image = img)  
	mywin.update()
	time.sleep(0.5)

mywin.mainloop()
