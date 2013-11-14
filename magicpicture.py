#!/usr/bin/env python3
from tkinter import *
import sys, os
from tkinter.filedialog import askopenfilename
class PicOpener(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=TOP)
        self.openphoto = []
        self.dispp = []
        self.numimg = 1
        Label(self, text="Press to open your Picture").pack()
        self.ass = Label(self, text='Opened files\n %s' % self.dispp)
        self.ass.pack()
        Button(self, text='OpenPicture', command=self.findpic).pack()

    def findpic(self):
        finame = askopenfilename(filetypes=(('Gif Files', '*.gif'), ('JPEG Files', '*.jpg;*.jpeg')))
        self.shownpic(finame)
        #print('fname=', finame)

    def shownpic(self, xn):
        win = Toplevel()
        win.title('Pic Window #%d' % self.numimg)
        self.numimg += 1
        img = PhotoImage(file=xn)
        self.openphoto.append(img)
        self.dispp.append(xn)
        upd = '\n'.join(self.dispp)
        self.ass.config(text=upd)
        can = Canvas(win)
        can.pack(fill=BOTH)
        can.config(width=img.width(), height=img.height())
        can.create_image(2, 2, image=img, anchor=NW)
        Button(win, text='Close Window', command=win.destroy).pack(side=BOTTOM)
        Label(win, text='I hope it\'s displaying your picture below!').pack(side=BOTTOM)
        print('xn=', self.dispp)
        print('connect', upd)

if __name__ == '__main__':
    root = Tk()
    mainframe = PicOpener(root)
    mainframe.pack()
    root.mainloop()
