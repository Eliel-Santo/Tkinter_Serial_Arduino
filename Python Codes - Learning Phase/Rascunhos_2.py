from tkinter import *
import tkinter as tk



# width x height + x_offset + y_offset:
width = 600
height = 600
x_offset = 30
y_offset = 30

String_dimension = str(width) + "x" + str(height) + "+" + str(x_offset) + "+" + str(y_offset)

print(String_dimension)


offset_image = 100

# Função para criação das Frames

def generic_frame(window, frame_width, frame_height, pos_x, pos_y,  text_generic_frame = "GenericFrame", anchor = 'n'):

    generic_frame_tkinter = tk.Frame(window, width=frame_width, height=frame_height,
                              bg='#ccffcc')  # , bg='#ccffcc'
    generic_frame_tkinter.place(x = pos_x, y = pos_y)

    edge_generic_frame = tk.LabelFrame(generic_frame_tkinter, text=text_generic_frame, bd=2, relief=GROOVE, labelanchor=anchor,
                                  cursor='gumby')
    edge_generic_frame.place(x=0, y=0, width=frame_width, height=frame_height)

def custom_isdigit(self):

    try:
        int(self)
        return True
    except ValueError: # Se não for inteiro
        return False # Ignora o teste para float

        try: # Teste por float
            float(self)
            return True
        except ValueError: # Se não for inteiro nem float
            return False


valor = '10'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '+10'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '-10'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '10.0'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '+10.0'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '-10.0'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))

valor = '10asd'
print("Valor = {0} - É digito? {1}".format(valor, custom_isdigit(valor)))





#
# root = tk.Tk()
# root.geometry(String_dimension)
# root.title("Prototype")
#
# width = 600
# height = 600
#
# generic_frame(root, 120 + 40, 30*8 + 30, width - 120 - 40 -20,  7 * 30 - 20, "Entrada")
#
# generic_frame(root, 2 * 120 + 40 + 20 + 80, 30*5 + 30, 20,  2 * 30 - 20, "Saída")
#
# generic_frame(root, 120 + 40, 30*3 + 40, width - 120 - 40 -20,  2 * 30 - 20, "Conexão Serial")
#
# generic_frame(root, 2 * 120 + 40 + 20 + 80, 30*2 + 30, 20,  14 * 30 - 20, "FilePath")
#
# generic_frame(root, 120 + 40*2, 25*3 + 40*2, 40 + 120 - 40,  8*30 - 0, "Operações")
#




# def generic_frame(window, generic_frame_width, generic_frame_height, generic_frame_pos_x, generic_frame_pos_y,  text_generic_frame = "GenericFrame", anchor = 'n'):

guto = tk.Tk()

width = 600
height = 650
String_dimension = str(width) + "x" + str(height) + "+" + str(x_offset) + "+" + str(y_offset)

guto.geometry(String_dimension)
guto.title("VISÃO DO AUGUSTO")

generic_frame(guto, 120*2 + 40 , 30*5 + 30, width - 120*2 - 40 -20,  7 * 30 - 20, "Intensidade", anchor='n')

generic_frame(guto, 2 * 120 + 40 + 20 - 30 , 30*10 + 30, 20,  2 * 30 - 20, "Operação")

generic_frame(guto, 120*2 + 40, 30*3 + 40, width - 120*2 - 40 -20,  2 * 30 - 20, "Conexão Serial")

generic_frame(guto, 4 * 120 + 40 + 20 + 20, 30*4 + 30, 20,  13 * 30 - 20, "Resultados")

# generic_frame(guto, 120 + 40*2, 25*3 + 40*2, 40 + 120 - 40,  8*30 - 0, "5")

generic_frame(guto, 2 * 120 + 40 + 20 + 80, 30*2 + 30, 20,   13 * 30 - 20 + 30*4 + 30, "FilePath")

# generic_frame(guto, 120, 25, 20 + 20, 14 * 30 - 15 + 15, "")

# print(range(4)[1])

for x in range(4):
    for y in range(3):
        generic_frame(guto, 120, 25, 20 + 10 + (120 + 20)*x, (13 + y) * 30 - 15 + 15, "" )


for i in range(3):
    generic_frame(guto, 120 , 25, width - 120 - 40, (8 + i) * 30 - 20, "")

    # if i == range(3)[-1]:
    #     generic_frame(guto, 120, 25, width - 120 - 40, (8 + i + 2) * 30 - 20, "")




tk.Button(guto, text="Aplicar/sendData").place(x=width - 120 - 40, y= (8 + 2 + 2) * 30 - 20, width=120, height=25)

tk.Button(guto, text="Novo Teste").place(x=0 + 40, y= 10, width=120, height=25)

tk.Button(guto, text="Desconectar").place(x=width - 120 - 40, y= height - 40, width=120, height=25)

def ShowChoice():
    a=1

v = tk.IntVar()

languages = [("Teste Parado",100),
    ("Teste Escuro", 101),
   	     ("Teste Calibração", 102),
    	     ("Teste Proteção", 103)]

for i in range(len(languages)):
    radio = tk.Radiobutton(guto,
                   text=languages[i][0],
                   padx = 20,
                   variable=v,
                   command=ShowChoice,
                   value=languages[i][1], indicatoron = 0)
    radio.place(x=20 + 20, y=(1 + i)*60 + 20*i, width=120*2 - 20, height= 30*2 )
    radio.config(font = '14')







# root.mainloop()
guto.mainloop()



