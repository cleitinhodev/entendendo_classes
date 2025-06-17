# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Importa o módulo Tkinter padrão (tk) e o módulo ttk (com widgets mais modernos)
import tkinter as tk
from tkinter import ttk


# Classe responsável por mostrar os resultados: dobro, triplo e raiz
class Resultados(tk.Frame):
    def __init__(self, master, caixa_de_texto):
        # Inicializa o Frame principal e guarda a referência do campo de entrada
        super().__init__(master)
        self.caixa_de_texto = caixa_de_texto

        # Cria um LabelFrame (uma caixa com título) para o dobro
        self.dobro_frame = tk.LabelFrame(self, text='Dobro:')
        self.dobro_frame.grid(row=0, column=0)  # Posiciona na linha 0, coluna 0

        # Rótulo que exibirá o valor do dobro
        self.rotulo_dobro = tk.Label(self.dobro_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_dobro.pack(padx=40, pady=2)

        # Cria o LabelFrame para o triplo
        self.triplo_frame = tk.LabelFrame(self, text='Triplo:')
        self.triplo_frame.grid(row=0, column=1)  # Coluna ao lado

        # Rótulo para mostrar o triplo
        self.rotulo_triplo = tk.Label(self.triplo_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_triplo.pack(padx=40, pady=2)

        # Cria o LabelFrame para a raiz quadrada
        self.raiz_frame = tk.LabelFrame(self, text='Raiz:')
        self.raiz_frame.grid(row=0, column=2)  # Próxima coluna

        # Rótulo para mostrar a raiz quadrada
        self.rotulo_raiz = tk.Label(self.raiz_frame, text='-', font=('Arial', 20), anchor=tk.CENTER, width=10)
        self.rotulo_raiz.pack(padx=40, pady=2)

    # Método que atualiza os três resultados com base no valor digitado
    def atualizar_tudo(self):
        valor = self.caixa_de_texto.get()  # Pega o valor digitado no campo de texto
        try:
            if valor == '':
                # Se estiver vazio, mostra apenas traços nos rótulos
                self.rotulo_dobro.config(text=f'-')
                self.rotulo_triplo.config(text=f'-')
                self.rotulo_raiz.config(text=f'-')
            else:
                # Chama a função que calcula os resultados
                resultados_finais = self.calcular_resultados(valor)

                # Atualiza os rótulos com os valores formatados com 2 casas decimais
                self.rotulo_dobro.configure(text=f'{resultados_finais[0]:.2f}')
                self.rotulo_triplo.configure(text=f'{resultados_finais[1]:.2f}')
                self.rotulo_raiz.configure(text=f'{resultados_finais[2]:.2f}')
        except ValueError:
            # Caso o valor digitado não seja um número válido
            self.rotulo_dobro.configure(text=f'-')
            self.rotulo_triplo.configure(text=f'-')
            self.rotulo_raiz.configure(text=f'-')

    # Função separada apenas para fazer os cálculos matemáticos
    def calcular_resultados(self, valor):
        valor = float(valor)  # Converte para número real
        return [valor * 2, valor * 3, valor ** 0.5]  # Retorna os três valores calculados


# Classe principal que representa o aplicativo
class App:
    def __init__(self, master):
        self.root = master  # Guarda a janela principal (root)
        self.root.title('Dobro, Triplo e Raiz Quadrada')  # Título da janela

        # Cria o campo de texto onde o usuário digita o número
        self.caixa_de_texto = ttk.Entry(self.root)
        self.caixa_de_texto.pack(padx=5, pady=5, fill='both')  # Posiciona e dimensiona
        self.caixa_de_texto.focus()  # Deixa o cursor já dentro da caixa ao iniciar

        # Cria o frame com os rótulos de resultado, passando o campo de entrada como referência
        self.resultados = Resultados(self.root, self.caixa_de_texto)
        self.resultados.pack()  # Exibe o frame na tela

        # Toda vez que uma tecla for solta, atualiza os resultados
        self.caixa_de_texto.bind("<KeyRelease>", lambda e: self.resultados.atualizar_tudo())


# Parte principal do programa que roda a aplicação
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal do Tkinter
    app = App(root)  # Cria uma instância da aplicação
    root.mainloop()  # Inicia o loop principal da interface (fica escutando os eventos)
