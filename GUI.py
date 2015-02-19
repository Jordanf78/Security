from tkinter import *

root = Tk()


def About():
    msgbox = Tk()
    msg = Label(msgbox,test = "File Integrity Checker version 1.0")
    msg.pack()
    mainloop()
    
def Help():
    msgbox = Tk()
    msg = Message(msgbox, text = "Helpwindowhere")
    msg.pack()
    mainloop()

##set window size + fixed size
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(800,600))

##Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Exit", command=root.quit())
helpmenu =Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=About)
helpmenu.add_command(label="Help", command=Help)

##Header Label
w = Label(root,text = "File Integrity Monitor 1.0")
w.pack()
root.mainloop()


