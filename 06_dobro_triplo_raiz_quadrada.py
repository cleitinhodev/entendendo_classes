# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import tkinter as tk
from tkinter import ttk


class Resultados(tk.Frame):
    def __init__(self, master, caixa_de_texto):
        super().__init__(master)
        self.caixa_de_texto = caixa_de_texto

        self.dobro_frame = tk.LabelFrame(self, text='Dobro:')
        self.dobro_frame.grid(row=0, column=0)
        self.rotulo_dobro = tk.Label(self.dobro_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_dobro.pack(padx=40, pady=2)

        self.triplo_frame = tk.LabelFrame(self, text='Triplo:')
        self.triplo_frame.grid(row=0, column=1)
        self.rotulo_triplo = tk.Label(self.triplo_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_triplo.pack(padx=40, pady=2)

        self.raiz_frame = tk.LabelFrame(self, text='Raiz:')
        self.raiz_frame.grid(row=0, column=2)
        self.rotulo_raiz = tk.Label(self.raiz_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_raiz.pack(padx=40, pady=2)

    def atualizar_tudo(self):
        valor = self.caixa_de_texto.get()
        try:
            if valor == '':
                self.rotulo_dobro.config(text=f'-')
                self.rotulo_triplo.config(text=f'-')
                self.rotulo_raiz.config(text=f'-')

            else:
                resultados_finais = self.calcular_resultados(valor)
                self.rotulo_dobro.configure(text=f'{resultados_finais[0]:.2f}')
                self.rotulo_triplo.configure(text=f'{resultados_finais[1]:.2f}')
                self.rotulo_raiz.configure(text=f'{resultados_finais[2]:.2f}')
        except ValueError:
            self.rotulo_dobro.configure(text=f'-')
            self.rotulo_triplo.configure(text=f'-')
            self.rotulo_raiz.configure(text=f'-')

    def calcular_resultados(self, valor):
        valor = float(valor)
        return [valor * 2, valor * 3, valor ** 0.5]


class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Dobro, Triplo e Raiz Quadrada')

        self.caixa_de_texto = ttk.Entry(self.root)
        self.caixa_de_texto.pack(padx=5, pady=5, fill='both')
        self.caixa_de_texto.focus()

        self.resultados = Resultados(self.root, self.caixa_de_texto)
        self.resultados.pack()

        self.caixa_de_texto.bind("<KeyRelease>", lambda e: self.resultados.atualizar_tudo())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
