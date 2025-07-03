# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

import tkinter as tk


class CampoNota(tk.Frame):
    def __init__(self, master, contador_de_notas):
        super().__init__(master)
        self['bd'] = 1
        self['relief'] = 'solid'
        self.nota_do_aluno = contador_de_notas

        self.rotulo_aluno = tk.Label(self, text=f'Nota {self.nota_do_aluno}:')
        self.rotulo_aluno.grid(row=0, column=0, padx=2, pady=2)
        self.entrada_de_nota = tk.Entry(self, width=45)
        self.entrada_de_nota.grid(row=0, column=1, padx=2, pady=2)

    def recolher_dados(self):
        return self.entrada_de_nota.get()


class TotalDeNotas(tk.Frame):
    def __init__(self, master, alunonota):
        super().__init__(master)
        self.nova_nota = None
        self['bd'] = 3
        self['relief'] = 'sunken'
        self.alunonota = alunonota
        self.linha_atual = 0
        self.contador_de_notas = 1
        self.botao_adicionar = tk.Button(self, text='               +               ', command=self.criar_registro)
        self.botao_adicionar.grid(row=self.linha_atual, padx=30)
        self.botao_remover = tk.Button(self, text='               -               ', command=self.remover_registro)
        self.botao_remover.grid(row=self.linha_atual, column=1, padx=30)
        self.lista_de_notas = []
        self.lista_de_objetos = []

    def criar_registro(self):
        self.nova_nota = self.alunonota(self, self.contador_de_notas)
        self.contador_de_notas += 1
        self.linha_atual += 1
        self.nova_nota.grid(row=self.linha_atual, columnspan=2)
        self.lista_de_objetos.append(self.nova_nota)

        self.linha_atual += 1
        self.botao_adicionar.grid(row=self.linha_atual)
        self.botao_remover.grid(row=self.linha_atual)

    def remover_registro(self):
        if self.lista_de_objetos:
            ultimo = self.lista_de_objetos.pop()
            ultimo.destroy()
            self.linha_atual -= 2
            self.contador_de_notas -= 1
            self.botao_adicionar.grid(row=self.linha_atual)
            self.botao_remover.grid(row=self.linha_atual)

    def mostrar_dados(self):
        self.lista_de_notas.clear()
        for i in self.lista_de_objetos:
            self.lista_de_notas.append(i.recolher_dados())
        return self.lista_de_notas


class CalcularMedia(tk.Frame):
    def __init__(self, master, total_de_notas):
        super().__init__(master)
        self['bd'] = 1
        self['relief'] = 'solid'
        self.total_de_notas = total_de_notas
        self.display = tk.Label(self, text='-', width=18, height=1, font=('Arial', 25))
        self.display.pack(padx=5, pady=5)
        self.btn_calc = tk.Button(self, text='Calcular Média', command=self.buscar_media)
        self.btn_calc.pack(padx=5, pady=5)

    def buscar_media(self):
        valores = self.total_de_notas.mostrar_dados()
        soma_total = 0.0
        try:
            for i in valores:
                i = float(i)
                soma_total += i
            media = soma_total / len(valores)
            self.display.config(text=f'{media:.2f}')
        except ValueError:
            self.display.config(text='Somente Números!')



class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Média Aritmética')

        self.total_de_notas = TotalDeNotas(self.root, CampoNota)
        self.total_de_notas.pack(padx=5, pady=5)

        self.calcular_media = CalcularMedia(self.root, self.total_de_notas)
        self.calcular_media.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
