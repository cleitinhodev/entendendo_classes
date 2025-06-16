# Crie um programa que escreva "Olá Mundo" na tela:

import tkinter as tk
from tkinter import ttk


class InterfaceDeTexto(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bg'] = '#000000'
        self['bd'] = 2
        self['relief'] = 'solid'
        self['width'] = 400
        self['height'] = 150
        self.pack_propagate(False)

        self.label_de_texto = tk.Label(self, text='Diga oi ao mundo!',
                                       font=('Arial', 20), fg='#00ff0c', background='#000000')
        self.label_de_texto.pack(expand=True)

    def mudar_texto(self, nova_mensagem):
        self.label_de_texto.configure(text=nova_mensagem)


class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Diga - Olá Mundo!')
        self.root.geometry('420x220')
        self.root['bg'] = '#703c88'
        self.root.grid_columnconfigure(0, weight=1)   # Expande caixa de texto para a linha completa

        self.interface_de_texto = InterfaceDeTexto(self.root)
        self.caixa_de_texto = ttk.Entry(self.root)
        self.caixa_de_texto.insert(0, "Olá Mundo")
        self.caixa_de_texto.focus()
        self.botao_de_oi = ttk.Button(self.root, text='Enviar', command=self.enviar_texto)

        self.interface_de_texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.caixa_de_texto.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.botao_de_oi.grid(row=1, column=1, padx=10, pady=10)

    def enviar_texto(self):
        self.interface_de_texto.mudar_texto(self.caixa_de_texto.get())


root = tk.Tk()
app = App(root)
root.mainloop()
