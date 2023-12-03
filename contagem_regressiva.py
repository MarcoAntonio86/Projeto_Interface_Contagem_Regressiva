from tkinter import *


def atualizar_contagem():
    global contador
    resultado_label.config(text=f'Contagem regressiva: {contador}')
    contador -= 1
    if contador >= 0:
        janela.after(1000, atualizar_contagem)


contador = 10


janela = Tk()
janela.title('Contagem Regressiva')
janela.geometry('400x300')


resultado_label = Label(janela, text=f'Contagem regressiva: {contador}')
resultado_label.pack(padx=10, pady=10)


atualizar_contagem()


janela.mainloop()
