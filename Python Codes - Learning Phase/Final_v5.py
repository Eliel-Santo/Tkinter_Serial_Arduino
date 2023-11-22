# import tkinter
import tkinter as tk
import serial
import json
import time
# from tkinter import *
import serial.tools.list_ports
from tkinter import filedialog




# https://github.com/portfoliocourses/python-example-code/blob/main/replace_specific.py
def replace_line(filename, line_number, text):
    # Open the file and read all the lines from the file into a list 'lines'
    with open(filename) as file:
        lines = file.readlines()

    print ("Linha: {} - Texto: {}".format(line_number, text))

    # if the line number is in the file, we can replace it successfully
    if (line_number <= len(lines)):

        # Replace the associated line in the list with the replacement text
        # (followed by a newline \n to end the line), we need to use line_number - 1
        # as the index because lists are zero-indexed in Python.

        if line_number == len(lines):
            lines[line_number - 1] = text
        else:
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


def read_line(filename, line_number, text):
    # Open the file and read all the lines from the file into a list 'lines'
    with open(filename) as file:
        lines = file.readlines()

    # if the line number is in the file, we can replace it successfully
    if (line_number <= len(lines)):

        # If the line number is in the file, we return it
        return lines[line_number - 1]

    # otherwise if the line number is past the length of the file, we can't
    # replace the line so output an error message instead
    else:

        # Output the line number that was requested to be replaced and the number
        # of lines the file actually has to inform the user
        print("Line", line_number, "not in file.")
        print("File has", len(lines), "lines.")


def custom_isdigit(number):

    try:
        int(number)
        return True
    except ValueError: # Se não for inteiro
        return False # Ignora o teste para float

        try: # Teste por float
            float(number)
            return True
        except ValueError: # Se não for inteiro nem float
            return False


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


# Função para criação das Frames

def generic_frame(generic_frame_width, generic_frame_height, generic_frame_pos_x, generic_frame_pos_y,  text_generic_frame = "GenericFrame", anchor = 'n'):

    generic_frame = tk.Frame(root, width=generic_frame_width, height=generic_frame_height,
                              bg='#ccffcc')  # , bg='#ccffcc'
    generic_frame.place(x = generic_frame_pos_x, y = generic_frame_pos_y)

    edge_generic_frame = tk.LabelFrame(generic_frame, text=text_generic_frame, bd=2, relief=tk.GROOVE, labelanchor='n',
                                  cursor='gumby')
    edge_generic_frame.place(x=0, y=0, width=generic_frame_width, height=generic_frame_height)






# Definição das Labels



# Definição da frame dos Valores de Entrada

height_frame_Input = 30*8 + 30
width_frame_Input =  120 + 40


frame_ReadValue = tk.Frame(root, height=height_frame_Input , width=width_frame_Input, bg='#ccffcc') # , bg='#ccffcc'
frame_ReadValue.place(x=width - 120 - 40 -20, y = 7 * 30 - 20)

edge_ReadValue = tk.LabelFrame(frame_ReadValue, text='Variáveis de Entrada', bd=2, relief=tk.GROOVE, labelanchor = 'n', cursor = 'gumby')
edge_ReadValue.place(x=0, y=0, width= width_frame_Input, height=height_frame_Input)

# Definições das labels de entrada


labels_entrada_variaveis = [value_read_string_1, value_read_string_2, value_read_string_3, value_read_string_4, value_read_string_5 ]

labels_entrada_starting_position = 7
for i in range(len(labels_entrada_variaveis)):
    tk.Entry(root,
             textvariable=value_read_string_1,
             fg='black',
             bg="white", bd=1, state="readonly", justify=tk.CENTER,
             relief=tk.GROOVE).place(x = width - 120 - 40, y=30* (labels_entrada_starting_position + i), width=120, height=25) # x = 40+ 120*3 + 20



# Função para definição da porta Serial
def serial_definition():
    print("Porta: {} - Baudrate: {}".format(clicked.get(), baudrate.get()))
    ser = serial.Serial(clicked.get()[0:5], baudrate.get(), timeout=None)

    Replace_text = "baudrate:" + str(baudrate.get())
    replace_line(folder_selected + "/" + "myfile.txt", quantidade_output + 1, Replace_text)


# Funções para deletar/substituir o texto temporario

def on_entry_click_Text_1(e):
    """function that gets called whenever entry is clicked"""
    if entry_variables[0].cget('fg') == 'grey':
        entry_variables[0].delete(0, "end")  # delete all the text in the entry
        entry_variables[0].insert(0, '')  # Insert blank for user input
        entry_variables[0].config(fg='black')

def on_focusout_Text_1(event):
    if entry_variables[0].get() == '':
        entry_variables[0].insert(0, var_atual_string_1.get())
        entry_variables[0].config(fg='grey')

def on_entry_click_Text_2(e):
    """function that gets called whenever entry is clicked"""
    if entry_variables[1].cget('fg') == 'grey':
        entry_variables[1].delete(0, "end")  # delete all the text in the entry
        entry_variables[1].insert(0, '')  # Insert blank for user input
        entry_variables[1].config(fg='black')

def on_focusout_Text_2(event):
    if entry_variables[1].get() == '':
        entry_variables[1].insert(0, var_atual_string_2.get())
        entry_variables[1].config(fg='grey')

def on_entry_click_Text_3(e):
    """function that gets called whenever entry is clicked"""
    if entry_variables[2].cget('fg') == 'grey':
        entry_variables[2].delete(0, "end")  # delete all the text in the entry
        entry_variables[2].insert(0, '')  # Insert blank for user input
        entry_variables[2].config(fg='black')

def on_focusout_Text_3(event):
    if entry_variables[2].get() == '':
        entry_variables[2].insert(0, var_atual_string_3.get())
        entry_variables[2].config(fg='grey')

def on_entry_click_Text_4(e):
    """function that gets called whenever entry is clicked"""
    if entry_variables[3].cget('fg') == 'grey':
        entry_variables[3].delete(0, "end")  # delete all the text in the entry
        entry_variables[3].insert(0, '')  # Insert blank for user input
        entry_variables[3].config(fg='black')

def on_focusout_Text_4(event):
    if entry_variables[3].get() == '':
        entry_variables[3].insert(0, var_atual_string_4.get())
        entry_variables[3].config(fg='grey')

def on_entry_click_Text_5(e):
    """function that gets called whenever entry is clicked"""
    if entry_variables[4].cget('fg') == 'grey':
        entry_variables[4].delete(0, "end")  # delete all the text in the entry
        entry_variables[4].insert(0, '')  # Insert blank for user input
        entry_variables[4].config(fg='black')

def on_focusout_Text_5(event):
    if entry_variables[4].get() == '':
        entry_variables[4].insert(0, var_atual_string_5.get())
        entry_variables[4].config(fg='grey')


# # Definição da frame dos Valores de Saída

height_frame_Output = 30*5 + 30
width_frame_Output =  2 * 120 + 40 + 20 + 80


frame_ReadValue = tk.Frame(root, height=height_frame_Output , width=width_frame_Output, bg='#ccffcc') # , bg='#ccffcc'
frame_ReadValue.place(x= 20, y = 2 * 30 - 20)

edge_ReadValue = tk.LabelFrame(frame_ReadValue, text='Variáveis de Saída', bd=2, relief=tk.GROOVE, labelanchor = 'n', cursor = 'gumby')
edge_ReadValue.place(x=0, y=0, width= width_frame_Output, height=height_frame_Output)


# Definição das Labels de saída


labels_saida_variaveis = ["Text 1", "Text 2", "Text 3", "Text 4", "Text 5"]

labels_saida_starting_position = 2
for i in range(len(labels_saida_variaveis)):
    tk.Label(root, text=labels_saida_variaveis[i]).place(x=40 + 0 * 40, y= (labels_saida_starting_position + i) * 30, width=120, height=25)


# Definição das Entry para os valores de Saída

entry_variables = []

entry_saida_variaveis = [var_atual_string_1, var_atual_string_2, var_atual_string_3, var_atual_string_4, var_atual_string_5 ]

entry_saida_funcoes =   [(on_entry_click_Text_1, on_focusout_Text_1),
                        (on_entry_click_Text_2, on_focusout_Text_2),
                        (on_entry_click_Text_3, on_focusout_Text_3),
                        (on_entry_click_Text_4, on_focusout_Text_4),
                        (on_entry_click_Text_5, on_focusout_Text_5)]

entry_saida_starting_position = 2
for i in range(len(entry_saida_variaveis)): # https://stackoverflow.com/questions/28608650/how-can-i-get-the-tkinter-entry-from-a-loop
    en = tk.Entry(root, bg="white", width=50, borderwidth=2)
    en.insert(0, entry_saida_variaveis[i].get())
    en.bind('<FocusIn>', entry_saida_funcoes[i][0])
    en.bind('<FocusOut>', entry_saida_funcoes[i][1])
    en.config(fg='grey')
    en.place(x=20 + 120 + 20 + 20, y=30 * (entry_saida_starting_position + i) , width=120, height=25)

    entry_variables.append(en)



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




    # Atualização do dropdown menu das portas seriais

    ports = serial.tools.list_ports.comports()

    # Caso não possua nenhuma porta conectada define um valor qualquer
    if len(ports) == 0:
        ports = ["None Defined"]

    drop_1 = tk.OptionMenu(root, clicked, *ports)
    drop_1.place(x=width - 120 - 40, y=2 * 30, width=120, height=25)

    if len(clicked.get()) > 10:
        clicked.set(clicked.get()[0:5])





    root.after(500, update_data)

update_data()


# def Testes_Variaveis_Saida(variavel_tkinter, limite_inferior, limite_superior, skip = False):
#     a = 1

def botao1():
    global data

    global var1
    global var2
    global var3
    global var4
    global var5

    # Definindo Default values in case of blank entries
    print("is the entry a digit? - " + str(custom_isdigit(entry_variables[0].get())))
    if custom_isdigit(entry_variables[0].get()) == False:
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

        if int(entry_variables[0].get()) > 10 or int(entry_variables[0].get()) < 0:
            forced_text1 = tk.Label(root, text="var ∉ [0,10]", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30*2 + 5, width=70, height=25)

        else:
            forced_text1 = tk.Label(root, text="", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30*2 + 5, width=70, height=25)

            var1 = int(entry_variables[0].get())  # Realiza a leitura da variável e transforma em inteiro

    if custom_isdigit(entry_variables[1].get()) == False: #Pode-se utilizar o seguinte caso queria alem de número: l2.get() == var_atual_string_2.get()
        forced_text2 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10 + 15, y=3*30 - 5, width=5, height=25)
    else:
        forced_text2 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text2.place(x=20 + 2 * 120 + 20 + 10 + 15, y=3*30 - 5, width=5, height=25)

        var2 = int(entry_variables[1].get())  # Realiza a leitura da variável e transforma em inteiro

    if custom_isdigit(entry_variables[2].get()) == False:
        forced_text3 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10 + 15, y=4*30 - 5, width=5, height=25)
    else:
        forced_text3 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text3.place(x=20 + 2 * 120 + 20 + 10 + 15, y=4*30 - 5, width=5, height=25)

        var3 = int(entry_variables[2].get())  # Realiza a leitura da variável e transforma em inteiro

    if custom_isdigit(entry_variables[3].get()) == False:
        forced_text4 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10 + 15, y=5*30 - 5, width=5, height=25)
    else:
        forced_text4 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text4.place(x=20 + 2 * 120 + 20 + 10 + 15, y=5*30 - 5, width=5, height=25)

        var4 = int(entry_variables[3].get())  # Realiza a leitura da variável e transforma em inteiro

    if custom_isdigit(entry_variables[4].get()) == False:
        forced_text5 = tk.Label(root, text="*", fg="red",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10 + 15, y=6*30 - 5, width=5, height=25)
    else:
        forced_text5 = tk.Label(root, text="", fg="black",
                                font="bold")  # Helvetica 12 bold italic
        forced_text5.place(x=20 + 2 * 120 + 20 + 10 + 15, y=6*30 - 5, width=5, height=25)

        var5 = int(entry_variables[4].get()) # Realiza a leitura da variável e transforma em inteiro

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
    header = "Operação; \t Leitura_1; \t Leitura_2; \t Leitura_3; \t Leitura_4; \t Leitura_5;"
    file_savedata.writelines(header)

    file_savedata = open(folder_savefile + "/" + "savefile.txt", "a+")
    print(folder_savefile)
    file_savedata.write('\n')


    text_line = "{0}; \t {1}; \t {2}; \t {3}; \t {4}; \t {5};".format(str(radio_var_1.get()), str(value_read_1.get()),
                                                                       str(value_read_2.get()), str(value_read_3.get()),
                                                                       str(value_read_4.get()), str(value_read_5.get()))

    file_savedata.writelines(text_line)



# Definição da frame dos Radio Buttons

height_frame_operacao = 25*3 + 40*2
width_frame_operacao =  120 + 40*2


frame = tk.Frame(root, height=height_frame_operacao , width=width_frame_operacao, bg='#ccffcc') # , bg='#ccffcc'
frame.place(x=40 + 120 - 40, y=8*30 - 0)

edge = tk.LabelFrame(frame, text='Operação', bd=2, relief=tk.GROOVE)
edge.place(x=0, y=0, width= width_frame_operacao, height=height_frame_operacao)


# Definição dos radio buttons

operacao_variaveis = [("Teste Parado", 0),
   	                  ("Teste Escuro", 1),
    	              ("Teste Calibração", 2),
                      ("Teste Proteção", 3)]


# for language, val in Operacao_variaveis:

starting_position_radiobutton = 9
for i in range (len(operacao_variaveis)):

    tk.Radiobutton(root,
                   text=operacao_variaveis[i][0],
                   indicatoron = 0,
                   padx = 20,
                   variable=radio_var_1,
                   command=ShowChoice,
                   value=operacao_variaveis[i][1]).place(x=40 + 120 , y=(starting_position_radiobutton + i)*30, width=120, height=25)


# Definição da frame do DropDown Menu


height_frame_operacao = 30*3 + 40
width_frame_operacao =  120 + 40


frame_DropDown = tk.Frame(root, height=height_frame_operacao , width=width_frame_operacao, bg='#ccffcc') # , bg='#ccffcc'
frame_DropDown.place(x=width - 120 - 40 -20, y=2 * 30 - 20)

edge_DropDown = tk.LabelFrame(frame_DropDown, text='Conexão Serial', bd=2, relief=tk.GROOVE, labelanchor = 'n', cursor = 'gumby')
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

edge_filepath = tk.LabelFrame(frame_filepath, text='FilePath', bd=2, relief=tk.GROOVE, labelanchor = 'nw', cursor = 'gumby')
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
    FilePath.strip()
    for i in range(len(FilePath)):
        if FilePath[i] == '\\':
            FilePath[i] = '/'

    if FilePath == '':
        # Do Nothing
        a = 1
    else:
        FilePath_String.set(FilePath)

    print(FilePath_String.get().strip())


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

