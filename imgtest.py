from tkinter import *

win = Tk()
imag = PhotoImage(file='/home/dexter/Documents/PP4E/Gui/gifs/ora-pp.gif')
Button(win, image=imag).pack()
win.mainloop()
#newwin = Toplevel()
#cov = PhotoImage('/home/dexter/Documents/PP4E/Gui/gifs/ora-lp4e.gif')
#canv = Canvas(newwin)
#canv.pack(fill=BOTH, side=TOP)
#canv.config(width=cov.width(), height=cov.height())
#canv.create_image(2, 2, image=cov, anchor=NW)
#Button(newwin, text='Close Window', command=newwin.quit).pack(side=BOTTOM)
#Label(newwin, text='I hope it\'s displaying your picture below!').pack(side=BOTTOM)
#Button(newwin, image=cov).pack()
#print('xn=')
#print('imag=')
#newwin.mainloop()