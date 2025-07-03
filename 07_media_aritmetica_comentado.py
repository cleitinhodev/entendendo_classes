# Importa o módulo tkinter, usado para criar interfaces gráficas em Python
import tkinter as tk


# Classe responsável por representar um campo de entrada de nota
class CampoNota(tk.Frame):
    def __init__(self, master, contador_de_notas):
        # Inicializa a classe base (Frame)
        super().__init__(master)

        # Define uma borda e um estilo visual
        self['bd'] = 1
        self['relief'] = 'solid'

        # Número da nota (usado para exibir "Nota 1", "Nota 2", etc.)
        self.nota_do_aluno = contador_de_notas

        # Rótulo que mostra o número da nota
        self.rotulo_aluno = tk.Label(self, text=f'Nota {self.nota_do_aluno}:')
        self.rotulo_aluno.grid(row=0, column=0, padx=2, pady=2)

        # Campo de entrada para o valor da nota
        self.entrada_de_nota = tk.Entry(self, width=45)
        self.entrada_de_nota.grid(row=0, column=1, padx=2, pady=2)

    # Método que retorna o valor digitado na entrada
    def recolher_dados(self):
        return self.entrada_de_nota.get()


# Classe que gerencia o conjunto de notas (adicionar/remover campos)
class TotalDeNotas(tk.Frame):
    def __init__(self, master, alunonota):
        super().__init__(master)
        self.nova_nota = None  # Referência temporária ao campo recém-criado

        # Estilo da moldura
        self['bd'] = 3
        self['relief'] = 'sunken'

        # Classe que representa o campo de nota (passada como argumento)
        self.alunonota = alunonota

        # Linha atual da grade
        self.linha_atual = 0

        # Contador para numerar as notas dinamicamente
        self.contador_de_notas = 1

        # Botão de adicionar novo campo de nota
        self.botao_adicionar = tk.Button(self, text='               +               ', command=self.criar_registro)
        self.botao_adicionar.grid(row=self.linha_atual, padx=30)

        # Botão de remover o último campo de nota
        self.botao_remover = tk.Button(self, text='               -               ', command=self.remover_registro)
        self.botao_remover.grid(row=self.linha_atual, column=1, padx=30)

        # Lista com os textos das notas
        self.lista_de_notas = []

        # Lista com os objetos criados dinamicamente
        self.lista_de_objetos = []

    # Cria um novo campo de nota na interface
    def criar_registro(self):
        # Cria o novo campo com o número correspondente
        self.nova_nota = self.alunonota(self, self.contador_de_notas)
        self.contador_de_notas += 1  # Atualiza o número da próxima nota

        self.linha_atual += 1  # Move para a próxima linha
        self.nova_nota.grid(row=self.linha_atual, columnspan=2)  # Adiciona o widget à grade

        self.lista_de_objetos.append(self.nova_nota)  # Salva o objeto criado

        # Atualiza a posição dos botões para ficarem abaixo dos campos
        self.linha_atual += 1
        self.botao_adicionar.grid(row=self.linha_atual)
        self.botao_remover.grid(row=self.linha_atual)

    # Remove o último campo de nota criado
    def remover_registro(self):
        if self.lista_de_objetos:
            ultimo = self.lista_de_objetos.pop()  # Remove da lista
            ultimo.destroy()  # Remove da interface

            self.linha_atual -= 2  # Volta duas linhas (campo + botões)
            self.contador_de_notas -= 1  # Decrementa o contador

            # Atualiza posição dos botões
            self.botao_adicionar.grid(row=self.linha_atual)
            self.botao_remover.grid(row=self.linha_atual)

    # Recupera os dados de todas as entradas de nota
    def mostrar_dados(self):
        self.lista_de_notas.clear()  # Limpa os dados antigos
        for i in self.lista_de_objetos:
            self.lista_de_notas.append(i.recolher_dados())  # Coleta os dados digitados
        return self.lista_de_notas


# Classe responsável por calcular e exibir a média
class CalcularMedia(tk.Frame):
    def __init__(self, master, total_de_notas):
        super().__init__(master)

        self['bd'] = 1
        self['relief'] = 'solid'

        # Referência ao objeto que contém os campos de nota
        self.total_de_notas = total_de_notas

        # Label onde a média será exibida
        self.display = tk.Label(self, text='-', width=18, height=1, font=('Arial', 25))
        self.display.pack(padx=5, pady=5)

        # Botão para iniciar o cálculo da média
        self.btn_calc = tk.Button(self, text='Calcular Média', command=self.buscar_media)
        self.btn_calc.pack(padx=5, pady=5)

    # Método chamado ao clicar no botão "Calcular Média"
    def buscar_media(self):
        valores = self.total_de_notas.mostrar_dados()  # Coleta os dados
        soma_total = 0.0  # Acumulador da soma

        try:
            # Converte cada valor para float e soma
            for i in valores:
                i = float(i)
                soma_total += i

            # Calcula a média
            media = soma_total / len(valores)

            # Atualiza o display com a média formatada com 2 casas decimais
            self.display.config(text=f'{media:.2f}')

        except ValueError:
            # Caso o usuário digite letras ou deixe algum campo vazio
            self.display.config(text='Somente Números!')


# Classe principal do programa que junta todos os componentes
class App:
    def __init__(self, master):
        self.root = master
        self.root.title('Média Aritmética')  # Título da janela

        # Cria a seção de notas (campos + botões de adicionar/remover)
        self.total_de_notas = TotalDeNotas(self.root, CampoNota)
        self.total_de_notas.pack(padx=5, pady=5)

        # Cria a seção de cálculo da média
        self.calcular_media = CalcularMedia(self.root, self.total_de_notas)
        self.calcular_media.pack(padx=5, pady=5)


# Ponto de entrada do programa
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = App(root)  # Instancia a aplicação
    root.mainloop()  # Inicia o loop da interface gráfica
