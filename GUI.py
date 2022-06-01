# customtkinter
import tkinter
import tkinter.messagebox
from tkinter import *
import sys

# Constructorvariables
title = ""
width = 0
height = 0

# set_Button
self = ""
x = 0
y = 0
text = ""
method = ""
innererUebergabeparameter = ""


# https://www.youtube.com/watch?v=yuuDJ3-EdNQ

# lambda function: https://www.youtube.com/watch?v=7u87KAO5-Ug
# passing functions https://www.studytonight.com/python-howtos/how-to-pass-a-method-as-an-argument-in-python

class Window:
    def __init__(self, title, width, height):
        self.frame = Tk()
        self.frame.title(title)
        self.frame.geometry(f"{width}x{height}")

    def set_button(self, x, y, text, method, *args):
        myButton = Button(master=self.frame, text=text, command= lambda: method(*args))
        myButton.place(x=x, y=y)

    def test_method(self, testtext):
        print(testtext)

    def set_label(self, x, y, text):
        myLabel = Label(master=self.frame, text=text)
        myLabel.place(x=x, y=y)

# funktioniert!!
#Findow = Window("test",500,500)
#Findow.set_button(100,100,"neu",Findow.test_method,"12kdk")
#mainloop()

if __name__ == "__main__":
    Window(title,width,height)
    Window.set_button(self, x, y, text, method, innererUebergabeparameter)
    Window.set_label(self, x, y, text)
