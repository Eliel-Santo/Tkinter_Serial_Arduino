# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import serial
import tkinter as tk
from tkinter import *
from tkinter.ttk import *



# Definitions for the Serial Communication
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()


def ledON():


    ser.write(b'1')

def ledOFF():

    ser.write(b'0')


def read_button():
    # global flag_temp
    # global string_button
    # print("before bytes waiting: " + str(ser.inWaiting()))
    # if ser.inWaiting() > 0:
    #     # string_button = str(ser.readline().decode('utf-8'))
    #     print("Bytes waiting1: " + str(ser.inWaiting()))
    #     print("Value waiting1: " + str(ser.readline().decode('utf-8')))
    #     string_button = str(ser.readline().decode('utf-8'))
    #     # flag_temp =False
    # else:
    #     print("Bytes waiting2: " + str(ser.inWaiting()))
    #     string_button = "0"
    # ser.flush()
    # return str(string_button)

    global string_button
    if ser.inWaiting() > 0:
        string_button = str(ser.read(1).decode("utf-8"))
        ser.flush()

    return string_button

def read_useless():
    a=4
    read_button()

# function for updating data
def show_data():
    global dualsense
    data_label_output.config(text=read_button())
    win.after(1000,show_data)

flag_temp = True
#Definitions for the tkinter

# Root widget to create window
win = tk.Tk()
# initialize window with title & minimum size
win.title("LedBultIn Control")
win.minsize(200,60)

# Button widget
ONbtn = tk.Button(win, bd=6, text="LED ON", command=ledON)
ONbtn.grid(column=1, row=2)
OFFbtn = tk.Button(win, bd=6, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=2)

# # Data input
# tk.Label(win, text="EmployeeID:").grid(row=0)
# tk.Label(win, text="Employee Name").grid(row=1)
# e = tk.Entry(win)
# en = tk.Entry(win)
# e.grid(row=0, column=1)
# en.grid(row=1, column=1)
#
# my_name=e.get() # read name
# print(my_name)

# CREATING TEXT IN TKINTER

photo = tk.PhotoImage(file = "C:/Users/eliel/Downloads/aviao.png")

string_button = "no_Read"
readbtn = tk.Button(win, bd=4, text="read_data", command=read_useless, image = photo).pack(side = TOP)
readbtn.grid(column=3, row=2)

# showing the data as a lable
data_label_output = tk.Label(win)
data_label_output.grid(row=1, column=1)

win.after_idle(show_data)


# start & open window continously
win.mainloop()

# Label widget
label = tk.Label(win, text="click to turn ON/OFF")
label.grid(column=1, row=1)





ser.close()