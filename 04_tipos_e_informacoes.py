# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

import tkinter as tk
from tkinter import ttk


class Vizualizando(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.area_de_envio = None

        self.tabela = ttk.Treeview(self, columns=("Tipo", "Confirmação"),
                                   show="headings")
        self.tabela.heading("Tipo", text="Tipo")
        self.tabela.heading("Confirmação", text="Confirmação")
        self.tabela.column("Tipo", anchor="w")
        self.tabela.column("Confirmação", anchor="center")

        self.tipo = self.tabela.insert("", "end", values=("Tipo Primitivo", ''))
        self.somente_espacos = self.tabela.insert("", "end", values=("Só tem espaços?", ''))
        self.numerico = self.tabela.insert("", "end", values=("É numérico?", ''))
        self.alfabetico = self.tabela.insert("", "end", values=("É alfabético?", ''))
        self.alfanumerico = self.tabela.insert("", "end", values=("É alfanumérico?", ''))
        self.maiusculas = self.tabela.insert("", "end", values=("Está em maiúsculas?", ''))
        self.minusculas = self.tabela.insert("", "end", values=("Está em minúsculas?", ''))
        self.captalizada = self.tabela.insert("", "end", values=("Está captalizada?", ''))

        self.tabela.pack()

    def set_area_de_envio(self, area_de_envio):
        self.area_de_envio = area_de_envio

    def processar_valor(self, valor):
        tipo = str(type(valor))
        somente_espacos = str(valor.isspace())
        numerico = str(valor.isnumeric())
        alfabetico = str(valor.isalpha())
        alfanumerico = str(valor.isalnum())
        maiusculas = str(valor.isupper())
        minusculas = str(valor.islower())
        captalizado = str(valor.istitle())

        self.tabela.item(self.tipo, values=("Tipo Primitivo", tipo))
        self.tabela.item(self.somente_espacos, values=("Só tem espaços?", somente_espacos))
        self.tabela.item(self.numerico, values=("É numérico?", numerico))
        self.tabela.item(self.alfabetico, values=("É alfabético?", alfabetico))
        self.tabela.item(self.alfanumerico, values=("É alfanumérico?", alfanumerico))
        self.tabela.item(self.maiusculas, values=("Está em maiúsculas?", maiusculas))
        self.tabela.item(self.minusculas, values=("Está em minúsculas?", minusculas))
        self.tabela.item(self.captalizada, values=("Está captalizada?", captalizado))


class AreaDeEnvio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bd'] = 1
        self['relief'] = 'solid'

        self.vizualizando = None

        self.caixa_de_valor = ttk.Entry(self, width=40)
        self.botao_de_verificacao = ttk.Button(self, text='Identificar', command=self.enviar_valor)

        self.caixa_de_valor.grid(row=0, column=0, padx=20, pady=10)
        self.botao_de_verificacao.grid(row=0, column=1, padx=20, pady=10)

    def set_vizualizando(self, vizualizando):
        self.vizualizando = vizualizando

    def enviar_valor(self):
        self.vizualizando.processar_valor(self.caixa_de_valor.get())


class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Tipo e Informações')

        self.vizualizando = Vizualizando(self.root)
        self.area_de_envio = AreaDeEnvio(self.root)

        self.vizualizando.set_area_de_envio(self.area_de_envio)
        self.area_de_envio.set_vizualizando(self.vizualizando)

        self.area_de_envio.pack(fill='both')
        self.vizualizando.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
