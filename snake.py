from tkinter import *
import random

root = Tk()
#window
root.geometry("610x600")
root.resizable(False,False)
#title
root.title("snake game indev")
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=1)
Grid.rowconfigure(root,1, weight=1)
#main frame
def mf():
	mainframe=LabelFrame(root,bg='black')
	mainframe.grid(row=1, column=0,rowspan=5, columnspan=5,sticky="EWNS")
	for i in range(0,32):
		Grid.columnconfigure(mainframe, i, weight=1)
		Grid.rowconfigure(mainframe, i, weight=1)
	for j in range(0,32):
		Label(mainframe,text="",bg='black').grid(row=j,column=j,sticky="NEWS")
	return(mainframe)
#food pos
def fpos():
	mf()
	x=random.randrange(0,32)
	y=random.randrange(0,32)
	food=Label(mf(),text="",bg='red')
	food.grid(row=x,column=y,sticky="NEWS")
#play button
playb=Button(root, text="play",command=fpos)
playb.grid(row=0, column=2,sticky='ew')
#high score
hs=Label(root, text='high score:')
hs.grid(row=0,column=0,sticky='ew')
#score
cs=Label(root, text='current score:')
cs.grid(row=0,column=4,sticky='ew')
root.mainloop()