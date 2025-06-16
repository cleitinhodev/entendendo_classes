# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

import tkinter as tk
from tkinter import ttk


class Central(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bd'] = 2
        self['relief'] = 'solid'

        self.sucessor = None
        self.antecessor = None

        self.caixa_central = ttk.Entry(self, width=30)
        self.caixa_central.pack(padx=10, pady=15)

    def set_valores(self, antecessor, sucessor):
        self.sucessor = sucessor
        self.antecessor = antecessor

    def atualizar_automaticamente(self):
        valor = self.caixa_central.get()
        try:
            if valor == '':
                self.sucessor.var_sucessor.set('-')
                self.antecessor.var_antecessor.set('-')
            else:
                valor = int(valor)
                maior = valor + 1
                menor = valor - 1
                self.sucessor.var_sucessor.set(f'{maior}')
                self.antecessor.var_antecessor.set(f'{menor}')

        except ValueError:
            self.sucessor.var_sucessor.set('-')
            self.antecessor.var_antecessor.set('-')

        self.after(100, self.atualizar_automaticamente)


class Sucessor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bd'] = 2
        self['relief'] = 'solid'
        self['bg'] = '#000000'

        self.var_sucessor = tk.StringVar()
        self.var_sucessor.set(f'-')

        self.rotulo_sucessor = tk.Label(self, textvariable=self.var_sucessor,
                                        font=("Arial", 15), width=3, bg='#000000', fg='#00ff0c')
        self.rotulo_sucessor.pack(padx=10, pady=10)


class Antecessor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bd'] = 2
        self['relief'] = 'solid'
        self['bg'] = '#000000'

        self.var_antecessor = tk.StringVar()
        self.var_antecessor.set('-')

        self.rotulo_antecessor = tk.Label(self, textvariable=self.var_antecessor,
                                          font=("Arial", 15), width=3, bg='#000000', fg='#00ff0c')
        self.rotulo_antecessor.pack(padx=10, pady=10)


class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Antecessor e Sucessor')

        self.central = Central(self.root)
        self.antecessor = Antecessor(self.root)
        self.sucessor = Sucessor(self.root)
        self.central.set_valores(self.antecessor, self.sucessor)

        self.antecessor.grid(row=0, column=0)
        self.central.grid(row=0, column=1)
        self.sucessor.grid(row=0, column=2)

        self.central.atualizar_automaticamente()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()