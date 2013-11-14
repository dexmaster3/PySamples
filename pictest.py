#!/usr/bin/env python3
from sys import argv
from tkinter import *
filename = argv[1] if len(argv) > 1 else 'ora-lp4e.gif'

direc = '/home/dexter/Documents/PP4E/Gui/gifs/'
root = Tk()
ass = direc + filename
print(ass)
cov = PhotoImage(file=direc + filename)
canv = Canvas(root)
canv.pack(fill=BOTH)
canv.config(width=cov.width(), height=cov.height())
canv.create_image(2, 2, image=cov, anchor=NW)
root.mainloop()
