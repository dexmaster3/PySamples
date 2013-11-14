from tkinter import *
from tkinter.messagebox import askokcancel
class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for x in picks:
            var = IntVar()
            chk = Checkbutton(self, text=x, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
    def state(self):
        return [var.get() for var in self.vars]

class Radiobar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.var = StringVar()
        self.var.set(picks[0])
        for x in picks:
            rad = Radiobutton(self, text=x, value=x, variable=self.var)
            rad.pack(side=side, anchor=anchor, expand=YES)
    def state(self):
        return self.var.get()

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        quitbut = Button(self, text='Quit', command=self.quit)
        quitbut.pack(side=LEFT, fill=BOTH, expand=YES)
    
    def quit(self):
        ques = askokcancel('Verify Exit', "Are you sure?")
        if ques: Frame.quit(self)

if __name__ == '__main__':
    root = Tk()
    lang = Checkbar(root, ['Python', 'C#', 'C++', "Java"])
    gui = Radiobar(root, ['win', 'x11', 'mac'], side=TOP, anchor=NW)
    tog = Checkbar(root, ["All"])

    root.title('Test')
    gui.pack(side=LEFT, fill=Y)
    lang.pack(side=TOP, fill=X)
    tog.pack(side=LEFT)
    lang.config(relief=GROOVE, bd=2)
    gui.config(relief=RIDGE, bd=3)

    def allstates():
        print(gui.state(), lang.state(), tog.state())

    Quitter(root).pack(side=RIGHT)
    Button(root, text="Peek", command=allstates).pack(side=RIGHT)
    root.mainloop()
