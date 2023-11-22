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

global var1
global var2
global var3
global var4
global var5

# Definindo os valores padrão (default) das variáveis

var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0


data = {"var1": var1, "var2": var2, "var3": var3, "var4": var4, "var5": var5}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
print(data)



# Information about Serial


# make sure the 'COM#' is set according the Windows Device Manager
# ser = serial.Serial('COM4', 9600, timeout=None)
# ser.reset_input_buffer()






# Variables
# Define as variáveis do tkinter como inteiros
# Definindo as variáveis de Saída
var_atual_1 = tk.IntVar()
var_atual_2 = tk.IntVar()
var_atual_3 = tk.IntVar()
var_atual_4 = tk.IntVar()
var_atual_5 = tk.IntVar()

#Definindo as variáveis de entrada
value_read_1 = tk.DoubleVar()
value_read_2 = tk.DoubleVar()
value_read_3 = tk.DoubleVar()
value_read_4 = tk.DoubleVar()
value_read_5 = tk.DoubleVar()


# Define os valores das variáveis com os valores iniciais
var_atual_1.set(var1)
var_atual_2.set(var2)
var_atual_3.set(var3)
var_atual_4.set(var4)
var_atual_5.set(var5)

value_read_1.set(1)
value_read_2.set(1)
value_read_3.set(1)
value_read_4.set(1)
value_read_5.set(1)

# Cria a variável de string
# Criando as Strings da variáveis de saída
var_atual_string_1 = tk.StringVar()
var_atual_string_2 = tk.StringVar()
var_atual_string_3 = tk.StringVar()
var_atual_string_4 = tk.StringVar()
var_atual_string_5 = tk.StringVar()

# Criando as Strings da variáveis de entrada
value_read_string_1 = tk.StringVar()
value_read_string_2 = tk.StringVar()
value_read_string_3 = tk.StringVar()
value_read_string_4 = tk.StringVar()
value_read_string_5 = tk.StringVar()



# Define os valores das Strings
# Definindo os valores da strings da variáveis de saída
var_atual_string_1.set("Valor Atual: " + str(var_atual_1.get()))
var_atual_string_2.set("Valor Atual: " + str(var_atual_2.get()))
var_atual_string_3.set("Valor Atual: " + str(var_atual_3.get()))
var_atual_string_4.set("Valor Atual: " + str(var_atual_4.get()))
var_atual_string_5.set("Valor Atual: " + str(var_atual_5.get()))

# Definindo os valores da strings da variáveis de entrada
value_read_string_1.set("Leitura Atual: " + str(value_read_1.get()))
value_read_string_2.set("Leitura Atual: " + str(value_read_2.get()))
value_read_string_3.set("Leitura Atual: " + str(value_read_3.get()))
value_read_string_4.set("Leitura Atual: " + str(value_read_4.get()))
value_read_string_5.set("Leitura Atual: " + str(value_read_5.get()))


# global Botao1
# global Botao2

# Definição das Labels
# Definição das Labels de saída
text1 = tk.Label(root, text="Text 1")
text1.place(x=20 + 0*40, y=30 , width=120, height=25)

text2 = tk.Label(root, text="Text 2")
text2.place(x=20 + 0*40, y= 2*30 , width=120, height=25)

text3 = tk.Label(root, text="Text 3")
text3.place(x=20 + 0*40, y= 3*30 , width=120, height=25)

text4 = tk.Label(root, text="Text 4")
text4.place(x=20 + 0*40, y= 4*30 , width=120, height=25)

text5 = tk.Label(root, text="Text 5")
text5.place(x=20 + 0*40, y= 5*30 , width=120, height=25)




# Definições das labels de entrada
intput_label_1 = tk.Label(root,
             textvariable=value_read_string_1,
             fg='White',
             bg="black")
intput_label_1.place(x=40+ 120*3 + 20, y=30*1, width=120, height=25)

intput_label_2 = tk.Label(root,
             textvariable=value_read_string_2,
             fg='White',
             bg="black")
intput_label_2.place(x=40+ 120*3 + 20, y=30*2, width=120, height=25)

intput_label_3 = tk.Label(root,
             textvariable=value_read_string_3,
             fg='White',
             bg="black")
intput_label_3.place(x=40+ 120*3 + 20, y=30*3, width=120, height=25)

intput_label_4 = tk.Label(root,
             textvariable=value_read_string_4,
             fg='White',
             bg="black")
intput_label_4.place(x=40+ 120*3 + 20, y=30*4, width=120, height=25)

intput_label_5 = tk.Label(root,
             textvariable=value_read_string_5,
             fg='White',
             bg="black")
intput_label_5.place(x=40+ 120*3 + 20, y=30*5, width=120, height=25)







# Funções para deletar/substituir o texto temporario

def on_entry_click_Text_1(e):
    """function that gets called whenever entry is clicked"""
    if l1.cget('fg') == 'grey':
        l1.delete(0, "end")  # delete all the text in the entry
        l1.insert(0, '')  # Insert blank for user input
        l1.config(fg='black')

def on_focusout_Text_1(event):
    if l1.get() == '':
        l1.insert(0, var_atual_string_1.get())
        l1.config(fg='grey')

def on_entry_click_Text_2(e):
    """function that gets called whenever entry is clicked"""
    if l2.cget('fg') == 'grey':
        l2.delete(0, "end")  # delete all the text in the entry
        l2.insert(0, '')  # Insert blank for user input
        l2.config(fg='black')

def on_focusout_Text_2(event):
    if l2.get() == '':
        l2.insert(0, var_atual_string_2.get())
        l2.config(fg='grey')

def on_entry_click_Text_3(e):
    """function that gets called whenever entry is clicked"""
    if l3.cget('fg') == 'grey':
        l3.delete(0, "end")  # delete all the text in the entry
        l3.insert(0, '')  # Insert blank for user input
        l3.config(fg='black')

def on_focusout_Text_3(event):
    if l3.get() == '':
        l3.insert(0, var_atual_string_3.get())
        l3.config(fg='grey')

def on_entry_click_Text_4(e):
    """function that gets called whenever entry is clicked"""
    if l4.cget('fg') == 'grey':
        l4.delete(0, "end")  # delete all the text in the entry
        l4.insert(0, '')  # Insert blank for user input
        l4.config(fg='black')

def on_focusout_Text_4(event):
    if l4.get() == '':
        l4.insert(0, var_atual_string_4.get())
        l4.config(fg='grey')

def on_entry_click_Text_5(e):
    """function that gets called whenever entry is clicked"""
    if l5.cget('fg') == 'grey':
        l5.delete(0, "end")  # delete all the text in the entry
        l5.insert(0, '')  # Insert blank for user input
        l5.config(fg='black')

def on_focusout_Text_5(event):
    if l5.get() == '':
        l5.insert(0, var_atual_string_5.get())
        l5.config(fg='grey')


l1 = tk.Entry(root, bg="white", width=50, borderwidth=2)
l1.place(x=20 + 120 + 20, y=30 , width=120, height=25)
l1.insert(0, var_atual_string_1.get())
l1.bind('<FocusIn>', on_entry_click_Text_1)
l1.bind('<FocusOut>', on_focusout_Text_1)
l1.config(fg = 'grey')

l2 = tk.Entry(root)
l2.place(x=20 + 120 + 20, y= 2*30 , width=120, height=25)
l2.insert(0, var_atual_string_2.get())
l2.bind('<FocusIn>', on_entry_click_Text_2)
l2.bind('<FocusOut>', on_focusout_Text_2)
l2.config(fg = 'grey')


l3 = tk.Entry(root)
l3.place(x=20 + 120 + 20, y= 3*30 , width=120, height=25)
l3.insert(0, var_atual_string_3.get())
l3.bind('<FocusIn>', on_entry_click_Text_3)
l3.bind('<FocusOut>', on_focusout_Text_3)
l3.config(fg = 'grey')


l4 = tk.Entry(root)
l4.place(x=20 + 120 + 20, y= 4*30 , width=120, height=25)
l4.insert(0, var_atual_string_4.get())
l4.bind('<FocusIn>', on_entry_click_Text_4)
l4.bind('<FocusOut>', on_focusout_Text_4)
l4.config(fg = 'grey')


l5 = tk.Entry(root)
l5.place(x=20 + 120 + 20, y= 5*30 , width=120, height=25)
l5.insert(0, var_atual_string_5.get())
l5.bind('<FocusIn>', on_entry_click_Text_5)
l5.bind('<FocusOut>', on_focusout_Text_5)
l5.config(fg = 'grey')



def update_data():


    # if (ser.inWaiting() > 0):
    #
    #     # ser.reset_input_buffer() # Apaga o buffer
    #     line = ser.readline().decode("utf-8")  # read a byte string
    #     # line = ser.read_until(b'\n')
    #     # ser.reset_input_buffer() # Apaga o buffer
    #
    #     print(line)
    #     #essas variáveis são temporárias, o que importa é a variável do tkinter
    #     read_1 = 0
    #     read_2 = 2
    #
    #     if len(line)>7:
    #
    #         i=0
    #         while line[i] != 'x':
    #             i=i+1
    #         if line[i+1] == 'x':
    #             read_1 = line[i + 2]
    #             read_2 = line[i + 3]
    #         else:
    #             read_1 = line[i + 1]
    #             read_2 = line[i + 2]
    #
    #
    #     value_read_1.set(int(read_1))
    #     value_read_2.set(int(read_2))
    #
    #
    # ser.reset_input_buffer() # Apaga o buffer

    value_read_1.set(value_read_1.get() + 1)
    value_read_2.set(value_read_2.get() + 1)
    value_read_3.set(value_read_3.get() + 1)
    value_read_4.set(value_read_5.get() + 1)
    value_read_5.set(value_read_5.get() + 1)

    value_read_string_1.set("Leitura Atual: " + str(value_read_1.get()))
    value_read_string_2.set("Leitura Atual: " + str(value_read_2.get()))
    value_read_string_3.set("Leitura Atual: " + str(value_read_3.get()))
    value_read_string_4.set("Leitura Atual: " + str(value_read_4.get()))
    value_read_string_5.set("Leitura Atual: " + str(value_read_5.get()))

    root.after(500, update_data)

update_data()



def botao1():
    global data

    global var1
    global var2
    global var3
    global var4
    global var5

    # Definindo Default values in case of blank entries
    print("is the entry a digit? - " + str(l1.get().isdigit()))
    if l1.get().isdigit() == False:
        forced_text1 = tk.Label(root, text="*",fg = "red",
		 font = "bold") #Helvetica 12 bold italic
        forced_text1.place(x=20 + 2*120 + 20 + 10, y=30 - 5, width=10, height=25)
    else:
        forced_text1 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text1.place(x=20 + 2 * 120 + 20 + 10, y=30 - 5, width=10, height=25)
        # forced_text1.destroy()

        # var1 = int(l1.get())  # Realiza a leitura da variável e transforma em inteiro

        if int(l1.get()) > 10:
            forced_text1 = tk.Label(root, text="Erro: var > 10", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10, y=30 + 5, width=70, height=25)

        else:
            forced_text1 = tk.Label(root, text="", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10, y=30 + 5, width=70, height=25)

            var1 = int(l1.get())  # Realiza a leitura da variável e transforma em inteiro

    if l2.get().isdigit() == False: #Pode-se utilizar o seguinte caso queria alem de número: l2.get() == var_atual_string_2.get()
        forced_text2 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10, y=2*30 - 5, width=10, height=25)
    else:
        forced_text2 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10, y=2*30 - 5, width=10, height=25)

        var2 = int(l2.get())  # Realiza a leitura da variável e transforma em inteiro

    if l3.get().isdigit() == False:
        forced_text3 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10, y=3*30 - 5, width=10, height=25)
    else:
        forced_text3 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10, y=3*30 - 5, width=10, height=25)

        var3 = int(l3.get())  # Realiza a leitura da variável e transforma em inteiro

    if l4.get().isdigit() == False:
        forced_text4 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10, y=4*30 - 5, width=10, height=25)
    else:
        forced_text4 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10, y=4*30 - 5, width=10, height=25)

        var4 = int(l4.get())  # Realiza a leitura da variável e transforma em inteiro

    if l5.get().isdigit() == False:
        forced_text5 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10, y=5*30 - 5, width=10, height=25)
    else:
        forced_text5 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10, y=5*30 - 5, width=10, height=25)

        var5 = int(l5.get()) # Realiza a leitura da variável e transforma em inteiro

    # Atualizando as leituras

    var_atual_1.set(var1)
    var_atual_2.set(var2)
    var_atual_3.set(var3)
    var_atual_4.set(var4)
    var_atual_5.set(var5)

    var_atual_string_1.set("Valor Atual: " + str(var_atual_1.get()))
    var_atual_string_2.set("Valor Atual: " + str(var_atual_2.get()))
    var_atual_string_3.set("Valor Atual: " + str(var_atual_3.get()))
    var_atual_string_4.set("Valor Atual: " + str(var_atual_4.get()))
    var_atual_string_5.set("Valor Atual: " + str(var_atual_5.get()))

    data = {"var1": var1, "var2": var2, "var3": var3, "var4": var4, "var5": var5}

    print(data)
    # data = json.dumps(data)  # Sending JSon
    # ser.write(bytes(data, 'utf-8'))



button1 = tk.Button(root,
                   text="Send Data",
                   fg="black",
                   command=botao1)
button1.place(x=40 + 120, y=7*30, width=120, height=25)





















root.mainloop()
