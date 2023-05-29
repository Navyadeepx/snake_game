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
mainframe=LabelFrame(root,bg='black')
mainframe.grid(row=1, column=0,rowspan=5, columnspan=5,sticky="EWNS")
for i in range(0,32):
	Grid.columnconfigure(mainframe, i, weight=1)
	Grid.rowconfigure(mainframe, i, weight=1)
for j in range(0,32):
	Label(mainframe,text="",bg='black').grid(row=j,column=j,sticky="NEWS")
#food pos
food=Label(mainframe,text="",bg='red')
def fck():
	f=0
	f+=1
	fposx=random.randrange(0,32)
	fposy=random.randrange(0,32)
	def fpos():
		if f==0:
			food.grid(row=fposx,column=fposy,sticky="NEWS")
		else:
			food.destroy()
			food.grid(row=fposx,column=fposy,sticky="NEWS")
	fpos()
#play button
playb=Button(root, text="play",command=fck)
playb.grid(row=0, column=2,sticky='ew')
#high score
hs=Label(root, text='high score:')
hs.grid(row=0,column=0,sticky='ew')
#score
cs=Label(root, text='current score:')
cs.grid(row=0,column=4,sticky='ew')
root.mainloop()