# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

import tkinter as tk
from tkinter import ttk


class DisplayDeEscrita(tk.Frame):
    def __init__(self, master, display_de_mensagem):
        super().__init__(master)
        self['bd'] = 2
        self['relief'] = 'solid'
        self['width'] = 325
        self['height'] = 250
        self.pack_propagate(False)

        self.display_de_mensagem = display_de_mensagem

        self.texto_de_ajuda = tk.Label(self, text='Diga, qual é o seu nome?', font=('Calisto MT', 20))
        self.caixa_de_nome = ttk.Entry(self, width=40)
        self.botao_de_envio = ttk.Button(self, text='Enviar', command=self.enviar_nome)

        self.texto_de_ajuda.pack(pady=10, expand=True)
        self.caixa_de_nome.pack(pady=10, expand=True)
        self.botao_de_envio.pack(pady=10, expand=True)

    def enviar_nome(self):
        self.display_de_mensagem.apresentar_nome(self.caixa_de_nome.get())


class DisplayDeMensagem(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bd'] = 2
        self['relief'] = 'solid'
        self['width'] = 175
        self['height'] = 250
        self['bg'] = '#000000'
        self.pack_propagate(False)

        self.mensagem_de_boas_vindas = tk.Label(self, text='', font=('Arial', 14), fg='white', bg='#000000')
        self.mensagem_de_boas_vindas.pack(expand=True)

    def apresentar_nome(self, novo_nome):
        nome = novo_nome
        if nome:
            self.mensagem_de_boas_vindas.configure(text=f'  Seja Bem-vindo(a)!  \n'
                                                        f'{novo_nome:^21}')
        else:self.mensagem_de_boas_vindas.configure(text=f'  Seja Bem-vindo(a)!  \n'
                                                         f'{"Desconhecido":^21}')


class Gerenciamento:
    def __init__(self, master):
        self.root = master
        self.root.title('Mensagem de Boas-Vindas')
        self.root.geometry('500x250')

        self.display_de_mensagem = DisplayDeMensagem(self.root)
        self.display_de_mensagem.grid(row=0, column=0)

        self.display_de_escrita = DisplayDeEscrita(self.root, self.display_de_mensagem)
        self.display_de_escrita.grid(row=0, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Gerenciamento(root)
    root.mainloop()
