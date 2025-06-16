#  Crie um programa que leia dois números e mostre a soma entre eles.

import tkinter as tk
from tkinter import ttk
from tkinter import font


class Emissor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.receptor = None

        self.caixa_valor_a = ttk.Entry(self)
        self.caixa_valor_b = ttk.Entry(self)

        self.label_de_soma = tk.Label(self, text='+')
        self.label_de_igual = tk.Label(self, text='=')

        self.botao_de_resultado = ttk.Button(self, text='Ver Resultado', command=self.calcular_valores)

        self.caixa_valor_a.grid(row=0, column=0, padx=10, pady=5)
        self.label_de_soma.grid(row=0, column=1, padx=10, pady=5)
        self.caixa_valor_b.grid(row=0, column=2, padx=10, pady=5)
        self.label_de_igual.grid(row=0, column=3, padx=10, pady=5)
        self.botao_de_resultado.grid(row=0, column=4, padx=10, pady=5)

    def set_receptor(self, receptor):
        self.receptor = receptor

    def calcular_valores(self):
        try:
            if not self.caixa_valor_a.get().strip() or not self.caixa_valor_b.get().strip():
                self.receptor.apresentar_resultado('Preencha os dois campos!')
                return
            valor_a = float(self.caixa_valor_a.get())
            valor_b = float(self.caixa_valor_b.get())
            resultado = valor_a + valor_b
            self.receptor.apresentar_resultado(resultado)
        except ValueError:
            self.receptor.apresentar_resultado('Digite apenas valores válidos (1, 20, 4.5...).')
        except AttributeError:
            print("Erro: Receptor não está configurado corretamente.")
        except TypeError:
            print("Erro de tipo inesperado.")


class Receptor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.emissor = None
        self['bd'] = 2
        self['relief'] = 'solid'

        self.fonte = font.Font(family='Arial', size=10, weight="bold")

        self.display_de_soma = tk.Label(self,
                                        text='Digite dois valores...',
                                        width=60, height=3,
                                        font=self.fonte)
        self.display_de_soma.pack(padx=10, pady=5)

    def set_emissor(self, emissor):
        self.emissor = emissor

    def apresentar_resultado(self, mensagem):
        if isinstance(mensagem, (int, float)):
            self.display_de_soma.config(text=f'Resultado: {mensagem}', fg='black')
        else:
            self.display_de_soma.config(text=mensagem, fg='red')


class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Soma Números')

        self.receptor = Receptor(self.root)
        self.emissor = Emissor(self.root)

        self.receptor.set_emissor(self.emissor)
        self.emissor.set_receptor(self.receptor)

        self.receptor.pack(pady=5)
        self.emissor.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
