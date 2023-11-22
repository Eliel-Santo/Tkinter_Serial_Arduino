# import random as random
# import matplotlib.pyplot as plt
#
# var_string = "x11111xx22222xx33333xx44444xx55555xx66666xx77777xx88888xx99999xx00000xx12345xx54321x"
# Input_Serial = var_string + var_string + var_string + str("\r\n")
#
#
# t = ''.join(Input_Serial.splitlines())
# Input_Serial = t
#
#
# print(Input_Serial[len(Input_Serial) - 1])
#
# rd_number = random.randrange(0, len(Input_Serial) - 1, 1)
#
# print("Random number between {0} and {1} is {2}".format(0, len(Input_Serial) - 1, rd_number))
#
# Input_Serial = Input_Serial[rd_number: len(Input_Serial)]
#
#
#
#
#
# # ########### Para copiar para o arquivo do tkinter COMECE aqui
# # Input_Serial - Deve ser o que foi lido da porta serial
#
#
# size_variable = 5
# ammount_variables = 12 # Esquema da variável: x12345x
# variables_recieved = [12345] * ammount_variables
#
# if len(Input_Serial) >= ammount_variables * (size_variable + 2):
#     buffer_recieved_treated = Input_Serial[len(Input_Serial) - ammount_variables * (size_variable + 2) : len(Input_Serial)]
#     # print(buffer_recieved_treated)
#
#     position = 0
#     for i in range(0, len(buffer_recieved_treated), size_variable + 2):
#         # print(buffer_recieved_treated[i+1:i+6])
#
#         if buffer_recieved_treated[i+1:i+6].isdigit():
#             variables_recieved[position] = int(buffer_recieved_treated[i+1:i+6])
#
#         position += 1
#
# else:
#     print("String Insuficiente")
#
# print("Variáveis recebidas pelo Serial: {}".format(variables_recieved))
#
#
#
# # ########### Para copiar para o arquivo do tkinter TERMINE aqui
#
#
#
#
# exit(0)
#
#
# aparicoes = [0] * 101
#
# for i in range(10000000):
#     rd_number = random.randrange(0, 100, 1)
#     aparicoes[rd_number] += 1
#
#
# print("Shape range: {1} & Shape aparicoes: {1}".format(len(range(0, 100, 1)), len(aparicoes) ))
#
# fig, ax = plt.subplots()
#
#
# ax.bar(range(0, 100, 1), aparicoes[0:100])
# ax.set_ylabel('Quantidade de vezes')
# ax.set_title('Verificação da Aleatoriedade do randomrange')
#
#
# plt.show()
#




# import tkinter as tk
#
#
# def switchButtonState():
#     if (botao[0]['state'] == tk.NORMAL):
#         botao[0]['state'] = tk.DISABLED
#     else:
#         botao[0]['state'] = tk.NORMAL
#
#
# app = tk.Tk()
# app.geometry("200x200")
# botao = []
# button1 = tk.Button(app, text="Python Button 1", state=tk.DISABLED)
# botao.append(button1)
# button2 = tk.Button(app, text="EN/DISABLE Button 1", command=switchButtonState)
# button1.pack()
# button2.pack()
#
# print(botao[0]['state'])
#
# app.mainloop()






import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root,
        text="""Choose a
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()

radio_1 = tk.Radiobutton(root,
               text="Python",
               padx = 20,
               variable=v,
               value=1)
radio_1.pack(anchor=tk.W)
radio_2 = tk.Radiobutton(root,
               text="Perl",
               padx = 20,
               variable=v,
               value=2).pack(anchor=tk.W)


print(radio_1["state"])

root.mainloop()














