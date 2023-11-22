from tkinter import filedialog
# from tkinter import *
import tkinter as tk

import os
from datetime import datetime



root = tk.Tk()
root.withdraw()


def replace_line(filename, line_number, text):
    # Open the file and read all the lines from the file into a list 'lines'
    with open(filename) as file:
        lines = file.readlines()

    print(lines)
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










#
# # folder_selected = filedialog.askdirectory()
#
# folder_selected = "C:/Users/eliel/Desktop/PlaceHolder - Copia (2)"
# file_savedata = open(folder_selected + "/" + "savefile.csv", "w")
# print(folder_selected)
#
#
# # Header
# header = "Operação; \t Leitura_1; \t Leitura_2; \t Leitura_3; \t Leitura_4; \t Leitura_5; \n"
# file_savedata.writelines(header)
#
# opera_atual = 0
# opera_antiga = 1
#
# if opera_atual != opera_antiga:
#     file_savedata.writelines(str(opera_atual) + "; \t 125; \t 125; \t 125; \t 125; \t 125; \n")
#     file_savedata.writelines("ubalubadubdub")
#
#



print("Folder: {}".format(os.path.dirname(os.path.abspath(__file__)) ))

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y %H.%M.%S")
filename =  dt_string

print("Archive Tittle: {}".format(filename ))

folder_selected = "C:/Users/eliel/Desktop/PlaceHolder - Copia (2)"
file = open(folder_selected + "/" + "myfile.txt", "r+")


print(read_line(folder_selected + "/" + "myfile.txt",1))




################# Início da lógica: Cria arquivo e pasta para salvar as medições

import os

directory_of_script = os.path.dirname(os.path.abspath(__file__)) # Gets the directory of the file (script)
directory_of_script = "C:/Users/eliel/Desktop/PlaceHolder - Copia (2)" # Quando for criar a aplicação de fato, é só comentar essa linha


os.makedirs(directory_of_script + str("/savefiles"), exist_ok=True) # Creates a directory on the folder of the script to save the datareading

directory_of_savefile = directory_of_script + '/savefiles'

file_existence = True
try:                            # Checks if the file exists
    f = open(directory_of_script + "/" + "forced.txt")
    file_existence = True
except FileNotFoundError:       # If the file doesn't exist
    file_existence = False
    print("File does not exist")
else:                           # If the file exists
    f.close()
    print("File Exists")

if file_existence == False:     # If the file does not exist, then creates it
    f = open(directory_of_script + "/" + "forced.txt","w")
    text_to_input = ['Text_1:1\n', 'Text_2:1\n', 'Text_3:3\n', 'Text_4:4\n', 'Text_5:5\n', 'baudrate:9600\n', 'FilePath:']
    text_to_input[len(text_to_input) - 1] = 'FilePath:' + directory_of_savefile
    f.writelines(text_to_input)


################# FIM da lógica: Cria arquivo e pasta para salvar as medições







f = open(folder_selected + "/" + "rascunho.txt","r+")
f.writelines("1\n")
f.writelines("2\n")
f = open(folder_selected + "/" + "rascunho.txt","r+")
f.writelines("3\n")



# Ideia:
# Identificar o path do arquivo
# Checar se há existe o arquivo mufile.txt - config
# Se não existir então cria ele e coloca os valores padrão


# Para implementação da ideia anterior utiliza-se a lib 'os':
# Poderia portanto criar uma nova pasta para salvar os arquivos de dados de entrada na pasta
# Se utilizar a lib 'os' não precisaria ter que tentar abrir o arquivo para ver se existe.
# https://www.python-engineer.com/posts/check-if-file-exists/

# Motivos para utilizar a lib 'os':
# Criação da pasta de salvação do dataset
# Evitaria ter que abrir arquivo para checar se existe
# Encontra automaticamente o endereço do arquivo do programa .py



i = 6
for i in range(0,11,2):
    print("{" + str(i) + "}; \\t {" + str(i + 1) + "}; ", end='')

# str(value_read_4.get())

for x in range(4):
    for y in range(3):
        print(y + x * range(4)[-1])