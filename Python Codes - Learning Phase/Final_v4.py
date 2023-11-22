import tkinter
import tkinter as tk
import serial
import json
import time
from tkinter import *
import serial.tools.list_ports
from tkinter import filedialog




# https://github.com/portfoliocourses/python-example-code/blob/main/replace_specific.py
def replace_line(filename, line_number, text):
    # Open the file and read all the lines from the file into a list 'lines'
    with open(filename) as file:
        lines = file.readlines()

    # if the line number is in the file, we can replace it successfully
    if (line_number <= len(lines)):

        # Replace the associated line in the list with the replacement text
        # (followed by a newline \n to end the line), we need to use line_number - 1
        # as the index because lists are zero-indexed in Python.
        lines[line_number - 1] = text + "\n"

        # Open the file in 'writing mode' using the 2nd argument "w", this means
        # that the file will be made blank, and any new text we write to the file
        # will become the new file contents.
        with open(filename, "w") as file:

            # Loop through the list of lines, write each of them to the file
            for line in lines:
                file.write(line)

    # otherwise if the line number is past the length of the file, we can't
    # replace the line so output an error message instead
    else:

        # Output the line number that was requested to be replaced and the number
        # of lines the file actually has to inform the user
        print("Line", line_number, "not in file.")
        print("File has", len(lines), "lines.")


# root = tk.Tk()
# root.withdraw()
#
# folder_selected = filedialog.askdirectory()

folder_selected = "C:/Users/eliel/Desktop/PlaceHolder - Copia (2)"

file = open(folder_selected + "/" + "myfile.txt", "r+")




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
global ports

ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#         print("{}: {} [{}]".format(port, desc, hwid))

# Caso não possua nenhuma porta conectada define um valor qualquer
if len(ports) == 0:
    ports = ["None Defined"]

# Definindo os valores padrão (default) das variáveis

# Linha
quantidade_output = 5
quantidade_baudrate = 1


Linha = file.readline(100)

if Linha.index(':') != 0:
    var1 = int(Linha[Linha.index(':') + 1 : len(Linha)])
else:
    var1 = 0


Linha = file.readline(100)

if Linha.index(':') != 0:
    var2 = int(Linha[Linha.index(':') + 1 : len(Linha)])
else:
    var2 = 0


Linha = file.readline(100)

if Linha.index(':') != 0:
    var3 = int(Linha[Linha.index(':') + 1 : len(Linha)])
else:
    var3 = 0


Linha = file.readline(100)

if Linha.index(':') != 0:
    var4 = int(Linha[Linha.index(':') + 1 : len(Linha)])
else:
    var4 = 0


Linha = file.readline(100)

if Linha.index(':') != 0:
    var5 = int(Linha[Linha.index(':') + 1 : len(Linha)])
else:
    var5 = 0


# var1 = 0
# var2 = 0
# var3 = 0
# var4 = 0
# var5 = 0


data = {"var1": var1, "var2": var2, "var3": var3, "var4": var4, "var5": var5, "Operacao": 0}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
print(data)



# Information about Serial


# make sure the 'COM#' is set according the Windows Device Manager
# ser = serial.Serial('COM4', 9600, timeout=None)
# ser.reset_input_buffer()








# Variables

# datatype of DropDown Menu
clicked = tk.StringVar()
baudrate = tk.IntVar()

# initial menu text
clicked.set("        ")
clicked.set("None")


Linha = file.readline(100)

if Linha.index(':') != 0:
    baudrate.set( int(Linha[Linha.index(':') + 1 : len(Linha)]) )
else:
    baudrate.set(9600)


# baudrate.set(9600)

# Dropdown menu options
options = [
    "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400", "57600",
    "115200", "230400", "250000", "500000", "1000000", "2000000"
]


# Definição da variável de FilePath

FilePath_String = tk.StringVar()
# FilePath_String.set("C:\\")

Linha = file.readline(10000)

if Linha.index(':') != 0:
    FilePath_String.set( Linha[Linha.index(':') + 1 : len(Linha)] )
else:
    FilePath_String.set("C:\\")

file.close()


# Define as variáveis do tkinter como inteiros
# Definindo as variáveis de Saída
var_atual_1 = tk.IntVar()
var_atual_2 = tk.IntVar()
var_atual_3 = tk.IntVar()
var_atual_4 = tk.IntVar()
var_atual_5 = tk.IntVar()

# Variável de saída do Radiobox
radio_var_1 = tk.IntVar()
radio_var_1.set(0)

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



# Definição da frame dos Valores de Entrada

height_frame_Input = 30*8 + 30
width_frame_Input =  120 + 40


frame_ReadValue = tk.Frame(root, height=height_frame_Input , width=width_frame_Input, bg='#ccffcc') # , bg='#ccffcc'
frame_ReadValue.place(x=width - 120 - 40 -20, y = 7 * 30 - 20)

edge_ReadValue = tk.LabelFrame(frame_ReadValue, text='Variáveis de Entrada', bd=2, relief=GROOVE, labelanchor = 'n', cursor = 'gumby')
edge_ReadValue.place(x=0, y=0, width= width_frame_Input, height=height_frame_Input)

# Definições das labels de entrada
intput_label_1 = tk.Entry(root,
             textvariable=value_read_string_1,
             fg='black',
             bg="white",bd=1,state="readonly", justify = tk.CENTER, relief = tkinter.GROOVE)
intput_label_1.place(x = width - 120 - 40, y=30*7, width=120, height=25) # x = 40+ 120*3 + 20

intput_label_2 = tk.Entry(root,
             textvariable=value_read_string_2,
             fg='black',
             bg="white",bd=1,state="readonly", justify = tk.CENTER, relief = tkinter.GROOVE)
intput_label_2.place(x = width - 120 - 40, y=30*8, width=120, height=25)

intput_label_3 = tk.Entry(root,
             textvariable=value_read_string_3,
             fg='black',
             bg="white",bd=1,state="readonly", justify = tk.CENTER, relief = tkinter.GROOVE)
intput_label_3.place(x = width - 120 - 40, y=30*9, width=120, height=25)

intput_label_4 = tk.Entry(root,
             textvariable=value_read_string_4,
             fg='black',
             bg="white",bd=1,state="readonly", justify = tk.CENTER, relief = tkinter.GROOVE)
intput_label_4.place(x = width - 120 - 40, y=30*10, width=120, height=25)

intput_label_5 = tk.Entry(root,
             textvariable=value_read_string_5,
             fg='black',
             bg="white",bd=1,state="readonly", justify = tk.CENTER, relief = tkinter.GROOVE)
intput_label_5.place(x = width - 120 - 40, y=30*11, width=120, height=25)





# Função para definição da porta Serial
def serial_definition():
    print("Porta: {} - Baudrate: {}".format(clicked.get(), baudrate.get()))
    ser = serial.Serial(clicked.get()[0:5], baudrate.get(), timeout=None)

    Replace_text = "baudrate:" + str(baudrate.get())
    replace_line(folder_selected + "/" + "myfile.txt", quantidade_output + 1, Replace_text)


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


# # Definição da frame dos Valores de Saída

height_frame_Output = 30*5 + 30
width_frame_Output =  2 * 120 + 40 + 20 + 80


frame_ReadValue = tk.Frame(root, height=height_frame_Output , width=width_frame_Output, bg='#ccffcc') # , bg='#ccffcc'
frame_ReadValue.place(x= 20, y = 2 * 30 - 20)

edge_ReadValue = tk.LabelFrame(frame_ReadValue, text='Variáveis de Saída', bd=2, relief=GROOVE, labelanchor = 'n', cursor = 'gumby')
edge_ReadValue.place(x=0, y=0, width= width_frame_Output, height=height_frame_Output)


# Definição das Labels de saída
text1 = tk.Label(root, text="Text 1")
text1.place(x=40 + 0*40, y= 2 * 30 , width=120, height=25)

text2 = tk.Label(root, text="Text 2")
text2.place(x=40 + 0*40, y= 3*30 , width=120, height=25)

text3 = tk.Label(root, text="Text 3")
text3.place(x=40 + 0*40, y= 4*30 , width=120, height=25)

text4 = tk.Label(root, text="Text 4")
text4.place(x=40 + 0*40, y= 5*30 , width=120, height=25)

text5 = tk.Label(root, text="Text 5")
text5.place(x=40 + 0*40, y= 6*30 , width=120, height=25)



# Definição das Entry para os valores de Saída

l1 = tk.Entry(root, bg="white", width=50, borderwidth=2)
l1.place(x=20 + 120 + 20 + 20, y=30 * 2 , width=120, height=25)
l1.insert(0, var_atual_string_1.get())
l1.bind('<FocusIn>', on_entry_click_Text_1)
l1.bind('<FocusOut>', on_focusout_Text_1)
l1.config(fg = 'grey')

l2 = tk.Entry(root)
l2.place(x=20 + 120 + 20 + 20, y= 3*30 , width=120, height=25)
l2.insert(0, var_atual_string_2.get())
l2.bind('<FocusIn>', on_entry_click_Text_2)
l2.bind('<FocusOut>', on_focusout_Text_2)
l2.config(fg = 'grey')


l3 = tk.Entry(root)
l3.place(x=20 + 120 + 20 + 20, y= 4*30 , width=120, height=25)
l3.insert(0, var_atual_string_3.get())
l3.bind('<FocusIn>', on_entry_click_Text_3)
l3.bind('<FocusOut>', on_focusout_Text_3)
l3.config(fg = 'grey')


l4 = tk.Entry(root)
l4.place(x=20 + 120 + 20 + 20, y= 5*30 , width=120, height=25)
l4.insert(0, var_atual_string_4.get())
l4.bind('<FocusIn>', on_entry_click_Text_4)
l4.bind('<FocusOut>', on_focusout_Text_4)
l4.config(fg = 'grey')


l5 = tk.Entry(root)
l5.place(x=20 + 120 + 20 + 20, y= 6*30 , width=120, height=25)
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

    if len(clicked.get()) > 10:
        clicked.set(clicked.get()[0:5])

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
        forced_text1.place(x=20 + 2*120 + 20 + 10 + 15, y=30*2 - 5, width=5, height=25)

        forced_text1 = tk.Label(root, text="", fg="red",
                                font="Helvetica 8 italic")  # Helvetica 12 bold italic
        forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 + 5, width=70, height=25)
    else:
        forced_text1 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30*2 - 5, width=5, height=25)
        # forced_text1.destroy()

        # var1 = int(l1.get())  # Realiza a leitura da variável e transforma em inteiro

        if int(l1.get()) > 10:
            forced_text1 = tk.Label(root, text="Erro: var > 10", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30*2 + 5, width=70, height=25)

        else:
            forced_text1 = tk.Label(root, text="", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30*2 + 5, width=70, height=25)

            var1 = int(l1.get())  # Realiza a leitura da variável e transforma em inteiro

    if l2.get().isdigit() == False: #Pode-se utilizar o seguinte caso queria alem de número: l2.get() == var_atual_string_2.get()
        forced_text2 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10 + 15, y=3*30 - 5, width=5, height=25)
    else:
        forced_text2 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10 + 15, y=3*30 - 5, width=5, height=25)

        var2 = int(l2.get())  # Realiza a leitura da variável e transforma em inteiro

    if l3.get().isdigit() == False:
        forced_text3 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10 + 15, y=4*30 - 5, width=5, height=25)
    else:
        forced_text3 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10 + 15, y=4*30 - 5, width=5, height=25)

        var3 = int(l3.get())  # Realiza a leitura da variável e transforma em inteiro

    if l4.get().isdigit() == False:
        forced_text4 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10 + 15, y=5*30 - 5, width=5, height=25)
    else:
        forced_text4 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10 + 15, y=5*30 - 5, width=5, height=25)

        var4 = int(l4.get())  # Realiza a leitura da variável e transforma em inteiro

    if l5.get().isdigit() == False:
        forced_text5 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10 + 15, y=6*30 - 5, width=5, height=25)
    else:
        forced_text5 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10 + 15, y=6*30 - 5, width=5, height=25)

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

    data = {"var1": var1, "var2": var2, "var3": var3, "var4": var4, "var5": var5, "Operacao":radio_var_1.get()}

    print(data)
    # data = json.dumps(data)  # Sending JSon
    # ser.write(bytes(data, 'utf-8'))


    # Update do valor da variável na memória do programa, memória = Bloco de Notas
    file = open(folder_selected + "/" + "myfile.txt", "r+")

    Replace_text = "Text_1:" + str(var_atual_1.get())
    replace_line(folder_selected + "/" + "myfile.txt", 1, Replace_text)

    Replace_text = "Text_2:" + str(var_atual_2.get())
    replace_line(folder_selected + "/" + "myfile.txt", 2, Replace_text)

    Replace_text = "Text_3:" + str(var_atual_3.get())
    replace_line(folder_selected + "/" + "myfile.txt", 3, Replace_text)

    Replace_text = "Text_4:" + str(var_atual_4.get())
    replace_line(folder_selected + "/" + "myfile.txt", 4, Replace_text)

    Replace_text = "Text_5:" + str(var_atual_5.get())
    replace_line(folder_selected + "/" + "myfile.txt", 5, Replace_text)

    file.close()



button1 = tk.Button(root,
                   text="Send Data",
                   fg="black",
                   command=botao1)
button1.place(x=width - 40 - 120, y=height - 40, width=120, height=25)




# Definição da Função do RadioButton - Opcional
def ShowChoice():

    folder_savefile = FilePath_String.get()
    file_savedata = open(folder_savefile + "/" + "savefile.txt", "r+")

    # Header
    header = "Operação; \t Leitura_1; \t Leitura_2; \t Leitura_3; \t Leitura_4; \t Leitura_5; \n"
    file_savedata.writelines(header)

    file_savedata = open(folder_savefile + "/" + "savefile.txt", "a+")
    print(folder_savefile)
    file_savedata.write('\n')


    text_line = "{0}; \t {1}; \t {2}; \t {3}; \t {4}; \t {5};\n".format(str(radio_var_1.get()), str(value_read_1.get()),
                                                                       str(value_read_2.get()), str(value_read_3.get()),
                                                                       str(value_read_4.get()), str(value_read_5.get()))

    file_savedata.writelines(text_line)



# Definição da frame dos Radio Buttons

height_frame_operacao = 25*3 + 40*2
width_frame_operacao =  120 + 40*2


frame = Frame(root, height=height_frame_operacao , width=width_frame_operacao, bg='#ccffcc') # , bg='#ccffcc'
frame.place(x=40 + 120 - 40, y=8*30 - 0)

edge = LabelFrame(frame, text='Operação', bd=5, relief=RIDGE)
edge.place(x=0, y=0, width= width_frame_operacao, height=height_frame_operacao)


# Definição dos radio buttons

operacao_variaveis = [("Teste Parado", 0),
   	                  ("Teste Escuro", 1),
    	              ("Teste Calibração", 2),
                      ("Teste Proteção", 3)]


# for language, val in Operacao_variaveis:
print(len(operacao_variaveis))
print(operacao_variaveis[0][0])
for i in range (len(operacao_variaveis)):
    print(i)
    tk.Radiobutton(root,
                   text=operacao_variaveis[i][0],
                   indicatoron = 0,
                   padx = 20,
                   variable=radio_var_1,
                   command=ShowChoice,
                   value=operacao_variaveis[i][1]).place(x=40 + 120 , y=(9 + i)*30, width=120, height=25)


#
#
# radio_0 = tk.Radiobutton(root,
#                text="Teste Parado      ",
#                padx = 20,
#                variable=radio_var_1,
#                value=0)
# radio_0.place(x=40 + 120 , y=9*30, width=120, height=25)
#
#
# radio_1 = tk.Radiobutton(root,
#                text="Teste Escuro      ",
#                padx = 20,
#                variable=radio_var_1,
#                command="ShowChoice",
#                value=1)
# radio_1.place(x=40 + 120, y=10*30, width=120, height=25)
#
#
# radio_2 = tk.Radiobutton(root,
#                text="Teste Calibração",
#                padx = 20,
#                variable=radio_var_1,
#                command="ShowChoice",
#                value=2)
# radio_2.place(x=40 + 120, y=11*30, width=120, height=25)
#
#
# radio_3 = tk.Radiobutton(root,
#                text="Teste Proteção   ",
#                padx = 20,
#                variable=radio_var_1,
#                command="ShowChoice",
#                value=3)
# radio_3.place(x=40 + 120, y=12*30, width=120, height=25)
#


# Definição da frame do DropDown Menu

height_frame_operacao = 30*3 + 40
width_frame_operacao =  120 + 40


frame_DropDown = tk.Frame(root, height=height_frame_operacao , width=width_frame_operacao, bg='#ccffcc') # , bg='#ccffcc'
frame_DropDown.place(x=width - 120 - 40 -20, y=2 * 30 - 20)

edge_DropDown = tk.LabelFrame(frame_DropDown, text='Conexão Serial', bd=2, relief=GROOVE, labelanchor = 'n', cursor = 'gumby')
edge_DropDown.place(x=0, y=0, width= width_frame_operacao, height=height_frame_operacao)





# Create Dropdown menu
drop_1 = tk.OptionMenu(root, clicked, *ports)
drop_1.place(x=width - 120 - 40, y=2 * 30, width=120, height=25)

drop_2 = tk.OptionMenu(root, baudrate, *options)
drop_2.place(x=width - 120 - 40, y=3 * 30, width=120, height=25)

# Create button, it will change label text
button_serial = tk.Button(root, text="Conectar", command=serial_definition)
button_serial.place(x=width - 120 - 40, y=4 * 30 + 10, width=120, height=25)





def on_entry_click_FilePath(e):
    """function that gets called whenever entry is clicked"""
    if FilePath_label_1.cget('fg') == 'grey':
        FilePath_label_1.delete(0, "end")  # delete all the text in the entry
        FilePath_label_1.insert(0, '')  # Insert blank for user input
        FilePath_label_1.config(fg='black')

def on_focusout_FilePath(event):

    if FilePath_label_1.get() == '':
        FilePath_label_1.insert(0, FilePath_String.get())
        FilePath_label_1.config(fg='grey')

# Definição da frame do FilePath

height_frame_filepath = 30*2 + 30
width_frame_filepath =  width_frame_Output


frame_filepath= tk.Frame(root, height=height_frame_filepath , width=width_frame_filepath, bg='#ccffcc') # , bg='#ccffcc'
frame_filepath.place(x= 20, y = 14 * 30 - 20)

edge_filepath = tk.LabelFrame(frame_filepath, text='FilePath', bd=2, relief=GROOVE, labelanchor = 'nw', cursor = 'gumby')
edge_filepath.place(x=0, y=0, width= width_frame_filepath, height=height_frame_filepath)

# # Definições das labels de FilePath

FilePath_label_1 = tk.Entry(root, bg="white", width=50, borderwidth=2)
FilePath_label_1.place(x=40 , y= 15 * 30 - 10 , width= width_frame_Output - 40 - 50, height=25)
FilePath_label_1.insert(0, FilePath_String.get())
FilePath_label_1.bind('<FocusIn>', on_entry_click_FilePath)
FilePath_label_1.bind('<FocusOut>', on_focusout_FilePath)
FilePath_label_1.config(fg = 'grey')

def FilePath_Change():
    FilePath = filedialog.askdirectory()
    for i in range(len(FilePath)):
        if FilePath[i] == '\\':
            FilePath[i] = '/'

    FilePath_String.set(FilePath)
    print(FilePath_String.get())


    Replace_text = "FilePath:" + str(FilePath_String.get())
    replace_line(folder_selected + "/" + "myfile.txt", quantidade_output + quantidade_baudrate + 1, Replace_text)

    FilePath_label_1.delete(0, "end")  # delete all the text in the entry
    FilePath_label_1.insert(0, '')  # Insert blank for user input

    FilePath_label_1.insert(0,FilePath_String.get())
    FilePath_label_1.config(fg='black')
# Create button, it will change the FilePath

button_FilePath = tk.Button(root, text="...", command=FilePath_Change, justify = tk.CENTER, anchor = tk.CENTER)
button_FilePath.place(x=width_frame_Output - 40, y = 15 * 30 - 10, width=25, height=25)










root.mainloop()


# FORMATAÇÃO DO ARQUIVO DE CONFIGURAÇÃO
# Text_1:5
# Text_2:6
# Text_3:7
# Text_4:8
# Text_5:9
# baudrate:9600
# FilePath:C:/Users/eliel/Desktop/PlaceHolder - Copia (2)

