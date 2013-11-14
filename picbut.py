from tkinter import *
gifloc = '/home/dexter/Documents/PP4E/Gui/gifs/'
root = Tk()
cover = PhotoImage(file=gifloc + 'ora-pp.gif')
Button(root, image=cover).pack()
root.mainloop()
