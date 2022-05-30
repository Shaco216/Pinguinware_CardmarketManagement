# customtkinter
import tkinter
import tkinter.messagebox
from tkinter import *
import customtkinter
from customtkinter import *
import sys

# https://www.youtube.com/watch?v=yuuDJ3-EdNQ

# lambda function: https://www.youtube.com/watch?v=7u87KAO5-Ug
# passing functions https://www.studytonight.com/python-howtos/how-to-pass-a-method-as-an-argument-in-python

class Window:
    def __init__(self, title, width, height):
        self.frame = Tk()
        self.frame.title(title)
        self.frame.geometry(f"{width}x{height}")

    def set_button(self, x, y, text, method):
        myButton = Button(master=self.frame, text=text, command= lambda: method)
        myButton.place(x=x, y=y)

    def test_method(self):
        print("testtesttest")