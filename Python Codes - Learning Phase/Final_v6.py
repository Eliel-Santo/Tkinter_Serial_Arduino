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
    with open(filename) as file_to_replace:
        lines = file_to_replace.readlines()

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
        with open(filename, "w") as file_to_replace:

            # Loop through the list of lines, write each of them to the file
            for line in lines:
                file_to_replace.write(line)

    # otherwise if the line number is past the length of the file, we can't
    # replace the line so output an error message instead
    else:

        # Output the line number that was requested to be replaced and the number
        # of lines the file actually has to inform the user
        print("Line", line_number, "not in file.")
        print("File has", len(lines), "lines.")


def read_line(filename, line_number):
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
global ports



ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#         print("{}: {} [{}]".format(port, desc, hwid))

# Caso não possua nenhuma porta conectada define um valor qualquer
if len(ports) == 0:
    ports = ["None Defined"]



# Information about Serial


# make sure the 'COM#' is set according the Windows Device Manager
# ser = serial.Serial('COM3', 9600, timeout=None)
# ser.reset_input_buffer()








# Variables

# Variable of DropDown Menu
clicked = tk.StringVar()
baudrate = tk.IntVar()

# initial menu text
clicked.set("        ")
clicked.set("None")



# Dropdown menu options
options = [
    "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400", "57600",
    "115200", "230400", "250000", "500000", "1000000", "2000000"
]


# Definição da variável de FilePath

FilePath_String = tk.StringVar()
# FilePath_String.set("C:\\")


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

# Definindo as variáveis de entrada
value_read_1 = tk.DoubleVar()
value_read_2 = tk.DoubleVar()
value_read_3 = tk.DoubleVar()
value_read_4 = tk.DoubleVar()
value_read_5 = tk.DoubleVar()


# Define os valores das variáveis com os valores iniciais





# Definindo os valores padrão (default) das variáveis

# Linha
quantidade_output = 5
quantidade_baudrate = 1

output_vars_tkinter = [var_atual_1, var_atual_2, var_atual_3, var_atual_4, var_atual_5]

for i in range(quantidade_output):
    Linha = file.readline(100)

    if Linha.index(':') != 0:
        output_vars_tkinter[i].set(int(Linha[Linha.index(':') + 1: len(Linha)]))
    else:
        output_vars_tkinter[i].set(0)


Linha = file.readline(100)

if Linha.index(':') != 0:
    baudrate.set( int(Linha[Linha.index(':') + 1 : len(Linha)]) )
else:
    baudrate.set(9600)

Linha = file.readline(10000)

if Linha.index(':') != 0:
    FilePath_String.set( Linha[Linha.index(':') + 1 : len(Linha)] )
else:
    FilePath_String.set("C:\\")

file.close()



data = {"var1": var_atual_1.get(), "var2": var_atual_2.get(), "var3": var_atual_3.get(), "var4": var_atual_4.get(), "var5": var_atual_5.get(), "Operacao": 0}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
print(data)


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
             textvariable=labels_entrada_variaveis[i],
             fg='black',
             bg="white", bd=1, state="readonly", justify=tk.CENTER,
             relief=tk.GROOVE).place(x = width - 120 - 40, y=30* (labels_entrada_starting_position + i), width=120, height=25) # x = 40+ 120*3 + 20



# Função para definição da porta Serial
def serial_definition():
    global ser
    global just_once
    global flag_fechar_serial

    flag_fechar_serial = 0

    print("Porta: {} - Baudrate: {}".format(clicked.get(), baudrate.get()))
    try:
        ser = serial.Serial(clicked.get()[0:5], baudrate.get(), timeout=None)
        just_once = True
    except ValueError:
        just_once = False
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

flag_fechar_serial = 0
just_once = False
def update_data():
    global just_once
    global ser
    #
    # clicked.set('COM3 ')
    # ser = serial.Serial(clicked.get(), int(baudrate.get()), timeout=None)
    # print(serial.Serial(clicked.get(), int(baudrate.get()), timeout=None).inWaiting())

    global flag_fechar_serial

    if flag_fechar_serial == 1:
        ser.reset_input_buffer()  # Apaga o buffer
        ser.close()
        flag_fechar_serial = 2

    elif flag_fechar_serial == 0:

        if clicked.get() != 'None' and just_once == True:
            # if just_once == True:
            #     # ser = serial.Serial(clicked.get()[0: 5], int(baudrate.get()), timeout=None)
            #     just_once = False



            if (ser.inWaiting() > 100):
                print("Quantidade de Bytes na porta serial: {0} de {1} necessários.".format(ser.inWaiting(), 12 * (5 + 2)))
                # ser.reset_input_buffer() # Apaga o buffer
                line = ser.readline().decode("utf-8")  # read a byte string
                # line = ser.read_until(b'\n')
                ser.reset_input_buffer() # Apaga o buffer

                print("Quantidade de Bytes na Linha: {0} de {1} necessários.".format(len(line), 12 * (5 + 2)))
                print(line)
                #essas variáveis são temporárias, o que importa é a variável do tkinter
                read_1 = 0
                read_2 = 2

                # ########### Para copiar para o arquivo do tkinter COMECE aqui

                size_variable = 5
                ammount_variables = 12  # Esquema da variável: x12345x
                variables_recieved = [12345] * ammount_variables

                t = ''.join(line.splitlines()) # Dave Campbell - https://stackoverflow.com/questions/45383938/cant-delete-r-n-from-a-string
                line = t

                if len(line) >= ammount_variables * (size_variable + 2):
                    buffer_recieved_treated = line[len(line) - ammount_variables * (size_variable + 2): len(
                        line)]
                    # print(buffer_recieved_treated)

                    position = 0
                    for i in range(0, len(buffer_recieved_treated), size_variable + 2):
                        # print(buffer_recieved_treated[i+1:i+6])

                        if custom_isdigit(buffer_recieved_treated[i + 1:i + 6]):
                            variables_recieved[position] = int(buffer_recieved_treated[i + 1:i + 6])
                            # print((buffer_recieved_treated[i + 1:i + 6]))
                            # print("Variables_Recieved[{0}]: {1}".format(position, variables_recieved[position]))

                        position += 1


                else:
                    print("String Insuficiente")


                print("Variáveis recebidas pelo Serial: {}".format(variables_recieved))

                # ########### Para copiar para o arquivo do tkinter TERMINE aqui


                value_read_1.set(int(variables_recieved[0]))
                value_read_2.set(int(variables_recieved[1]))
                value_read_3.set(int(variables_recieved[2]))
                value_read_4.set(int(variables_recieved[3]))
                value_read_5.set(int(variables_recieved[4]))




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











    # value_read_1.set(value_read_1.get() + 1)
    # value_read_2.set(value_read_2.get() + 1)
    # value_read_3.set(value_read_3.get() + 1)
    # value_read_4.set(value_read_5.get() + 1)
    # value_read_5.set(value_read_5.get() + 1)

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





    root.after(30, update_data)

update_data()



def botao1():
    global data


    # Definindo Default values in case of blank entries
    # print("is the entry a digit? - " + str(custom_isdigit(entry_variables[0].get())))

    def Testes_Variaveis_Saida(variavel_entry_tkinter, variavel_int_tkinter, limite_inferior=0, limite_superior=255,
                               skip=False):

        if custom_isdigit(variavel_entry_tkinter.get()) == False:
            forced_text1 = tk.Label(root, text="*", fg="red",
                                    font="bold")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 - 5, width=5, height=25)

            forced_text1 = tk.Label(root, text="", fg="red",
                                    font="Helvetica 8 italic")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 + 5, width=70, height=25)
        else:
            forced_text1 = tk.Label(root, text="", fg="black",
                                    font="bold")  # Helvetica 12 bold italic
            forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 - 5, width=5, height=25)
            # forced_text1.destroy()

            # var1 = int(l1.get())  # Realiza a leitura da variável e transforma em inteiro
            if skip == True:
                variavel_int_tkinter.set(
                    int(variavel_entry_tkinter.get()))  # Realiza a leitura da variável e transforma em inteiro
            else:

                if int(variavel_entry_tkinter.get()) > limite_superior or int(
                        variavel_entry_tkinter.get()) < limite_inferior or skip:
                    forced_text1 = tk.Label(root, text="var ∉ [0,10]", fg="red",
                                            font="Helvetica 8 italic")  # Helvetica 12 bold italic
                    forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 + 5, width=70, height=25)

                else:
                    forced_text1 = tk.Label(root, text="", fg="red",
                                            font="Helvetica 8 italic")  # Helvetica 12 bold italic
                    forced_text1.place(x=20 + 2 * 120 + 20 + 10 + 15, y=30 * 2 + 5, width=70, height=25)

                    variavel_int_tkinter.set(
                        int(variavel_entry_tkinter.get()))  # Realiza a leitura da variável e transforma em inteiro



    Testes_Variaveis_Saida(entry_variables[0],output_vars_tkinter[0], limite_inferior=0, limite_superior=255, skip=False)
    Testes_Variaveis_Saida(entry_variables[1],output_vars_tkinter[1], limite_inferior=0, limite_superior=255, skip=True)
    Testes_Variaveis_Saida(entry_variables[2],output_vars_tkinter[2], limite_inferior=0, limite_superior=255, skip=True)
    Testes_Variaveis_Saida(entry_variables[3],output_vars_tkinter[3], limite_inferior=0, limite_superior=255, skip=True)
    Testes_Variaveis_Saida(entry_variables[4],output_vars_tkinter[4], limite_inferior=0, limite_superior=255, skip=True)


    var_atual_string_1.set("Valor Atual: " + str(var_atual_1.get()))
    var_atual_string_2.set("Valor Atual: " + str(var_atual_2.get()))
    var_atual_string_3.set("Valor Atual: " + str(var_atual_3.get()))
    var_atual_string_4.set("Valor Atual: " + str(var_atual_4.get()))
    var_atual_string_5.set("Valor Atual: " + str(var_atual_5.get()))

    data = {"var1": var_atual_1.get(), "var2": var_atual_2.get(), "var3": var_atual_3.get(), "var4": var_atual_4.get(), "var5": var_atual_5.get(), "Operacao":radio_var_1.get()}

    print(data)
    if clicked.get() != 'None':
        data = json.dumps(data)  # Sending JSon
        ser.write(bytes(data, 'utf-8'))


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

    global radio_button_tkinter

    def switchButtonState(tkinter_button_variable):
        if (tkinter_button_variable['state'] == tk.NORMAL):
            tkinter_button_variable['state'] = tk.DISABLED
        else:
            tkinter_button_variable['state'] = tk.NORMAL


    for i in range(len(radio_button_tkinter)):
        # print("Operação: {0} -> i = {1}".format(radio_var_1.get(), i))
        if radio_var_1.get() == i:

            if i == len(radio_button_tkinter) - 1: # Ou seja, se estiver no último valor
                radio_button_tkinter[i]['state'] = tk.DISABLED
                radio_button_tkinter[0]['state'] = tk.NORMAL
            else: # Se tiver em qualquer posição além da última

                radio_button_tkinter[i]['state'] = tk.DISABLED
                radio_button_tkinter[i + 1]['state'] = tk.NORMAL



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
radio_button_tkinter = []
for i in range (len(operacao_variaveis)):

    radio_buttons = tk.Radiobutton(root,
                   text=operacao_variaveis[i][0],
                   indicatoron = 0,
                   padx = 20,
                   variable=radio_var_1,
                   command=ShowChoice, state=tk.DISABLED,font="Arial 10 bold",
                   value=operacao_variaveis[i][1])
    radio_buttons.place(x=40 + 120 , y=(starting_position_radiobutton + i)*30, width=120, height=25)
    radio_button_tkinter.append(radio_buttons)

radio_button_tkinter[1].config(state = 'normal')

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



# Teste do botão de fechar serial



def close_serial():
    # global ser
    global flag_fechar_serial
    flag_fechar_serial = 1
    print(clicked.get())

    # ser.close()


# Create button, it will change label text
button_serial_close = tk.Button(root, text="Desconectar", command=close_serial)
button_serial_close.place(x=width - 40 - 120*2 -20, y=height - 40, width=120, height=25)








root.mainloop()


# FORMATAÇÃO DO ARQUIVO DE CONFIGURAÇÃO
# Text_1:5
# Text_2:6
# Text_3:7
# Text_4:8
# Text_5:9
# baudrate:9600
# FilePath:C:/Users/eliel/Desktop/PlaceHolder - Copia (2)


