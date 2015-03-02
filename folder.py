#!/usr/bin/env python
# Chirag Patel 
from tkinter import *
from tkinter import filedialog

root = Tk()
select_directory = filedialog.askdirectory(parent = root, initialdir = "/", title="Select a directory")
if len(select_directory) > 0:
    print (("Choose %s") % (select_directory))


#Selecting a file
from tkinter import *
from tkinter import filedialog

root = Tk()
file = filedialog.askopenfile(parent=root,mode='rb',title="Choose file")
if file != None:
    data = file.read()
    file.close()
    print ("I got %d bytes from this file." % len(data))


# "Save as" dialog:
from tkinter import *
from tkinter import filedialog

formats = [("JPEG", "JPG"), ("*.gif", "*.png")]

root = Tk()
file_name = filedialog.asksaveasfilename(parent=root,filetypes = formats ,title = "Save the image as...")
if len(file_name ) > 0:
    print ("Now saving in %s" % nomFichier)
