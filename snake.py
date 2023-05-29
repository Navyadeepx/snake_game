from tkinter import *

root = Tk()
#window
root.geometry("600x600")
#title
root.title("snake game indev")
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=1)
#play button
playb=Button(root, text="play")
playb.grid(row=0, column=2,sticky='ew')
#main frame
mainframe=LabelFrame(root)
mainframe.grid(row=1, column=0,rowspan=5, columnspan=5)
#high score
hs=Label(root, text='high score:')
hs.grid(row=0,column=0,sticky='ew')
#score
cs=Label(root, text='current score:')
cs.grid(row=0,column=4,sticky='ew')
root.mainloop()