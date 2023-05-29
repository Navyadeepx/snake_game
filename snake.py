from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("snake game indev")
Button(root, text="play").grid(row=0, column=0)
mainframe=LabelFrame(root)
mainframe.grid(row=1, column=0,rowspan=5, columnspan=5)
root.mainloop()