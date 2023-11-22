import tkinter as tk
import serial
import json
import time
from tkinter import *
import random

root = tk.Tk()
# width x height + x_offset + y_offset:
width = 600
height = 600
x_offset = 30
y_offset = 30

String_dimension = str(width) + "x" + str(height) + "+" + str(x_offset) + "+" + str(y_offset)

print(String_dimension)
root.geometry(String_dimension)
root.title("Prototype")

offset_image = 100

# Creating Json
global data

global led1
global led2
global led1_pwm
global led2_pwm

led1 = 0
led2 = 0
led1_pwm = 0
led2_pwm = 0

data = {"led1": led1, "led2": led1, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
print(data)



# Information about Serial


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9600, timeout=None)
# ser.reset_input_buffer()






# Variables

Button_1_read = tk.IntVar()
Button_2_read = tk.IntVar()
Analog_1_read = tk.IntVar()

Button_1_read.set(1)
Button_2_read.set(1)
Analog_1_read.set(1)

Button_1_text = tk.StringVar()
Button_2_text = tk.StringVar()
Analog_1_text = tk.StringVar()

Button_1_text.set("Button1: ")
Button_2_text.set("Button2: ")
Analog_1_text.set("Analog1: ")

# global Botao1
# global Botao2



########################### Sliders

# Slider for LED1
w1 = tk.Scale(root, from_=0, to=255, tickinterval=10, orient=tk.HORIZONTAL)
w1.set(128)
w1.place(x=20, y=30 + 30*3, width=120, height=40)

# Slider for LED2
w2 = tk.Scale(root, from_=0, to=255, tickinterval=10, orient=tk.HORIZONTAL)
w2.set(128)
w2.place(x=40+120, y=30 + 30*3, width=120, height=40)

########################## Serial Data for use in functions

# https://stackoverflow.com/questions/2785821/is-there-an-easy-way-in-python-to-wait-until-certain-condition-is-true
def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate: return True
    time.sleep(period)
  return False


####################### Functions for the buttons

# def update_data():
#     global data
#     global led1
#     global led2
#     global led1_pwm
#     global led2_pwm
#
#     print("FUNCAO UPDATE_DATA")
#     data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
#     print(data)


def slider_led_1():
    print(w1.get())

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led1_pwm = w1.get()
    def update_data():
        global data
        global led1
        global led2
        global led1_pwm
        global led2_pwm

        print("FUNCAO UPDATE_DATA")
        data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
        print(data)
        data = json.dumps(data)  # Sending JSon
        ser.write(bytes(data, 'utf-8'))

    update_data()

def slider_led_2():
    print(w2.get())

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led2_pwm = w2.get()

    def update_data():
        global data
        global led1
        global led2
        global led1_pwm
        global led2_pwm

        print("FUNCAO UPDATE_DATA")
        data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
        print(data)
        data = json.dumps(data)  # Sending JSon
        ser.write(bytes(data, 'utf-8'))

    update_data()

def led1_on():
    print("led1_On")

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led1 = 1
    # data["led1"] = 1
    # data["led1"] = int(data["led1"].replace(str(0),str(1)))



    print("FUNCAO UPDATE_DATA")
    data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
    print(data)
    data = json.dumps(data)  # Sending JSon
    ser.write(bytes(data, 'utf-8'))
    ser.flush()





def led2_on():
    print("led2_on")

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led2 = 1
    def update_data():
        global data
        global led1
        global led2
        global led1_pwm
        global led2_pwm

        print("FUNCAO UPDATE_DATA")
        data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
        print(data)
        data = json.dumps(data)  # Sending JSon
        ser.write(bytes(data, 'utf-8'))
        ser.flush()

    update_data()

def led1_off():
    print("led1_off")

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led1 = 0
    def update_data():
        global data
        global led1
        global led2
        global led1_pwm
        global led2_pwm

        print("FUNCAO UPDATE_DATA")
        data = {'led1': led1, 'led2': led2, 'led1_pwm': led1_pwm, 'led2_pwm': led2_pwm}
        print(data)
        data = json.dumps(data)  # Sending JSon
        ser.write(bytes(data, 'utf-8'))

    update_data()

def led2_off():
    print("led2_off")

    global data
    global led1
    global led2
    global led1_pwm
    global led2_pwm

    led2 = 0

    print("FUNCAO UPDATE_DATA")
    data = {"led1": led1, "led2": led2, "led1_pwm": led1_pwm, "led2_pwm": led2_pwm}
    print(data)
    data = json.dumps(data)  # Sending JSon
    ser.write(bytes(data, 'utf-8'))


def Open_Serial():
    ser.open()
    print("ser.open()")

def Close_Serial():
    ser.close()
    print("ser.close()")


########################### Labels

# Images

logo1 = tk.PhotoImage(file="C:/Users/eliel/Downloads/led_red (1).png")
image1 = tk.Label(root,
             compound = tk.CENTER,
             image=logo1).place(x=20, y=30 + 200)

logo2 = tk.PhotoImage(file="C:/Users/eliel/Downloads/led_yellow (1).png")
image2 = tk.Label(root,
             compound = tk.CENTER,
             image=logo2).place(x=40+120+25, y=30 + 200)


l = tk.Label(root,
             text="Led1",
             fg='White',
             bg="blue")
l.place(x=20, y=30 + 0, width=120, height=25)

l2 = tk.Label(root,
             text="Led2",
             fg='White',
             bg="blue")
l2.place(x=40+120, y=30 +0, width=120, height=25)

label_B1 =  tk.Label(root,
             textvariable=Button_1_read,
             fg='White',
             bg="black")
label_B1.place(x=40+120*2 + 20, y=30 + 0, width=120, height=25)

label_B2 =  tk.Label(root,
             textvariable=Button_2_read,
             fg='White',
             bg="black")
label_B2.place(x=40+120*2 + 20, y=30 + 30*1, width=120, height=25)

label_Analog =  tk.Label(root,
             textvariable=Analog_1_read,
             fg='White',
             bg="black")
label_Analog.place(x=40+120*2 + 20, y=30 + 30*2, width=120, height=25)

i = 1

def update_data():
    # Button_1_read.set(Button_1_read.get() + 1)
    # Button_2_read.set(Button_2_read.get() + 1)
    # Analog_1_read.set(Analog_1_read.get() + 1)
    #
    # Button_1_text.set("Button1: " + str(Button_1_read))
    # Button_2_text.set("Button1: " + str(Button_2_read))
    # Analog_1_text.set("Button1: " + str(Analog_1_read))

    if (ser.inWaiting() > 0):

        # ser.reset_input_buffer() # Apaga o buffer
        line = ser.readline().decode("utf-8")  # read a byte string
        # line = ser.read_until(b'\n')
        # ser.reset_input_buffer() # Apaga o buffer

        print(line)

        Botao1 = 0
        Botao2 = 2

        if len(line)>7:

            i=0
            while line[i] != 'x':
                i=i+1
            if line[i+1] == 'x':
                Botao1 = line[i + 2]
                Botao2 = line[i + 3]
            else:
                Botao1 = line[i + 1]
                Botao2 = line[i + 2]


        #
        # if line[i+1] == 'x':
        #     Botao1 = line[i + 1]
        #     Botao2 = line[i + 2]

        # Botao1 = line[i+1]
        # Botao2 = line[i+2]
        #
        #
        Button_1_read.set(int(Botao1))
        Button_2_read.set(int(Botao2))




    ser.reset_input_buffer() # Apaga o buffer

    Analog_1_read.set(Analog_1_read.get() + 1)

    label_B1.config(text=Button_1_read)
    label_B2.config(text=Button_2_read)
    root.after(10, update_data)

update_data()

########################### Buttons

# Buttons for LED1

button1 = tk.Button(root,
                   text="On",
                   fg="green",
                   command=led1_on)
button1.place(x=20, y=30 + 30, width=120, height=25)

button2 = tk.Button(root,
                   text="Off",
                   fg="red",
                   command=led1_off)
button2.place(x=20, y=30 + 30*2, width=120, height=25)

# Buttons for LED2

button3 = tk.Button(root,
                   text="On",
                   fg="green",
                   command=led2_on)
button3.place(x=40+120, y=30 + 30, width=120, height=25)

button4 = tk.Button(root,
                   text="Off",
                   fg="red",
                   command=led2_off)
button4.place(x=40+120, y=30 + 30*2, width=120, height=25)

# Slider Button LED 2

button_slider_led1 = tk.Button(root,
                   text="Slider",
                   fg="black",
                   command=slider_led_1)
button_slider_led1.place(x=20, y=30 + 30*5, width=120, height=25)

# Slider Button LED 2

button_slider_led2 = tk.Button(root,
                   text="Slider",
                   fg="black",
                   command=slider_led_2)
button_slider_led2.place(x=40+120, y=30 + 30*5, width=120, height=25)



button_text_update = tk.Button(root,
                   text="Update",
                   fg="black",
                   command=update_data)
button_text_update.place(x=40+120*2 + 20, y=30 + 30*5, width=120, height=25)


Serial_Open = tk.Button(root,
                   text="Serial Open",
                   fg="black",
                   command=Open_Serial)
Serial_Open.place(x=width-x_offset-120*3 - 20*2, y=height-y_offset-25, width=120, height=25)

Serial_Close = tk.Button(root,
                   text="Serial Close",
                   fg="black",
                   command=Close_Serial)
Serial_Close.place(x=width-x_offset-120*2 - 20, y=height-y_offset-25, width=120, height=25)




########################### Set to be at the buttom right corner of the screen
QuitButton = tk.Button(root,
                   text="Quit",
                   fg="red",
                   command=quit)
QuitButton.place(x=width-x_offset-120, y=height-y_offset-25, width=120, height=25)











root.mainloop()