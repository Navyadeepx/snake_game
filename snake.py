from tkinter import *
import random
root = Tk()
#window
root.geometry("800x800")
root.resizable(False,False)
#title
root.title("snake game indev")
for i in range(5):
	Grid.columnconfigure(root, i, weight=1)
Grid.rowconfigure(root,1, weight=1)
#main frame
mainframe=LabelFrame(root,bg='black')
mainframe.grid(row=1, column=0,rowspan=5, columnspan=5,sticky="EWNS",padx=5,pady=5)
for i in range(32):
	Grid.columnconfigure(mainframe, i, weight=1)
	Grid.rowconfigure(mainframe, i, weight=1)
for j in range(32):
	Label(mainframe,text="",bg='black').grid(row=j,column=j,sticky="NEWS")
#food pos
x=random.randrange(32)
y=random.randrange(32)
food=Label(mainframe,text="",bg='red')
food.grid(row=x,column=y,sticky="NEWS")
cord=(x,y)
#snake pos
x=random.randrange(32)
y=random.randrange(32)
if cord[0]==x and cord[1]==y:
	x=(x+1)//1
	y=(y+1)//1
snake=Label(mainframe,text="",bg='green')
snake.grid(row=x,column=y,sticky="NEWS")
#high score
hs=Label(root, text='high score:',padx=10)
hs.grid(row=0,column=0,sticky='w')
#score
cs=Label(root, text='current score:')
cs.grid(row=0,column=4,sticky='e',padx=10)
root.mainloop()