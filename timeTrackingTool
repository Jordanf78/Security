#!/usr/bin/python

from tkinter import *

def __init__():
    if (state):
        global timer
        # Every time this function is called,
        # we will increment 1 centisecond (1/100 of a second)
        timer[2] += 1

        # (Every 100 centisecond is equal to 1 second)
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        # (Every 60 seconds is equal to 1 min)
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        # We create our time string
        timeString = pattern.format(timer[0], timer[1], timer[2])

        # Update the timeText Label box with the current time
        timeText.configure(text = timeString)

    # Call the __init__() function after 1 centisecond
    root.after(10, __init__)

# To start the time tracking tool
def start():
    global state
    state = True

# To pause the time tracking tool
def pause():
    global state
    state = False

# To reset the timer to 00:00:00
def reset():
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')

# To exist the time tracking tool
def exist():
    root.destroy()

#def count():
#    global state
#    state = pause - start
#    state = False


# Simple status flag
# False mean the timer is not running
# True means the timer is running
state = False

root = Tk()
root.wm_title('Time Tracking Tool')
root.configure(background= 'light blue')

# Our time structure [minute, second, centsec]
timer = [0, 0, 0]
# The format is padding all the
pattern = "{0:02d}:{1:02d}:{2:02d}"

# Create a timeText Label (a text box)
timeText = Label(root, text= "00:00:00", bg= 'light blue', font=("Times New Roman", 30))
timeText.pack()

start = Button(root, text='Start',bg='light blue', command=start)
start.pack()

pause = Button(root, text='Pause',bg='light blue', command=pause)
pause.pack()

reset = Button(root, text='Reset',bg='light blue', command=reset)
reset.pack()

quit = Button(root, text='Quit',bg='light blue', command=exist)
quit.pack()

#count = Button(root, text = "cout", command=count)
#count.pack()

__init__()
root.mainloop()
