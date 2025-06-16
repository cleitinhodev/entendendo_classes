# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

import tkinter as tk               # Importa o módulo tkinter para criação da interface gráfica
from tkinter import ttk            # Importa ttk para usar widgets com estilo moderno

# Classe que representa o campo central onde o usuário digita o número
class Central(tk.Frame):
    def __init__(self, master):
        super().__init__(master)    # Inicializa o frame pai
        self['bd'] = 2              # Define a borda do frame com largura 2
        self['relief'] = 'solid'   # Define o estilo da borda como sólida

        self.sucessor = None        # Inicialmente, variável que vai armazenar o widget Sucessor está vazia
        self.antecessor = None      # Inicialmente, variável que vai armazenar o widget Antecessor está vazia

        # Cria uma caixa de texto (Entry) para o usuário digitar o número, com largura 30 caracteres
        self.caixa_central = ttk.Entry(self, width=30)
        # Adiciona a caixa na interface com espaçamento interno horizontal e vertical
        self.caixa_central.pack(padx=10, pady=15)

    # Método para associar os widgets Antecessor e Sucessor a esta classe
    def set_valores(self, antecessor, sucessor):
        self.sucessor = sucessor        # Guarda referência para o widget Sucessor
        self.antecessor = antecessor    # Guarda referência para o widget Antecessor

    # Método que atualiza automaticamente os valores do sucessor e antecessor
    def atualizar_automaticamente(self):
        valor = self.caixa_central.get()   # Pega o texto digitado na caixa central
        try:
            if valor == '':                # Se o campo estiver vazio
                # Define os textos dos widgets sucessor e antecessor para "-"
                self.sucessor.var_sucessor.set('-')
                self.antecessor.var_antecessor.set('-')
            else:
                valor = int(valor)         # Tenta converter o texto para inteiro
                maior = valor + 1          # Calcula o sucessor
                menor = valor - 1          # Calcula o antecessor
                # Atualiza os textos dos widgets com os valores calculados
                self.sucessor.var_sucessor.set(f'{maior}')
                self.antecessor.var_antecessor.set(f'{menor}')

        except ValueError:                 # Caso o valor não seja um número inteiro válido
            # Exibe "-" para indicar erro/entrada inválida
            self.sucessor.var_sucessor.set('-')
            self.antecessor.var_antecessor.set('-')

        # Agenda a execução deste método novamente após 100 milissegundos (0.1 segundo)
        self.after(100, self.atualizar_automaticamente)

# Classe que representa o widget que exibe o sucessor
class Sucessor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)          # Inicializa o frame pai
        self['bd'] = 2                    # Define borda com largura 2
        self['relief'] = 'solid'          # Define estilo da borda como sólida
        self['bg'] = '#000000'            # Define fundo preto para o frame

        # Cria uma StringVar que vai armazenar e atualizar o texto do Label dinamicamente
        self.var_sucessor = tk.StringVar()
        self.var_sucessor.set(f'-')       # Inicializa o texto com '-'

        # Cria o Label que exibirá o sucessor, vinculado à variável StringVar
        self.rotulo_sucessor = tk.Label(
            self,
            textvariable=self.var_sucessor,
            font=("Arial", 15),           # Define fonte Arial tamanho 15
            width=3,                      # Define largura fixa para o label
            bg='#000000',                 # Fundo preto para o label
            fg='#00ff0c'                  # Cor do texto verde neon
        )
        self.rotulo_sucessor.pack(padx=10, pady=10)  # Adiciona o label no frame com espaçamento

# Classe que representa o widget que exibe o antecessor (muito parecido com Sucessor)
class Antecessor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)          # Inicializa o frame pai
        self['bd'] = 2                    # Define borda com largura 2
        self['relief'] = 'solid'          # Define estilo da borda como sólida
        self['bg'] = '#000000'            # Fundo preto para o frame

        # Cria uma StringVar para atualizar o texto do Label dinamicamente
        self.var_antecessor = tk.StringVar()
        self.var_antecessor.set('-')      # Inicializa o texto com '-'

        # Cria o Label que exibirá o antecessor, vinculado à variável StringVar
        self.rotulo_antecessor = tk.Label(
            self,
            textvariable=self.var_antecessor,
            font=("Arial", 15),           # Fonte Arial tamanho 15
            width=3,                      # Largura fixa
            bg='#000000',                 # Fundo preto
            fg='#00ff0c'                  # Texto verde neon
        )
        self.rotulo_antecessor.pack(padx=10, pady=10)  # Adiciona o label no frame com espaçamento

# Classe principal que cria a aplicação e monta a interface
class App:
    def __init__(self, master):
        self.root = master                # Guarda a janela principal (Tk)
        self.root.title('Antecessor e Sucessor')  # Define o título da janela

        # Cria as três áreas principais da interface
        self.central = Central(self.root)        # Campo central para digitar
        self.antecessor = Antecessor(self.root)  # Widget que mostra o antecessor
        self.sucessor = Sucessor(self.root)      # Widget que mostra o sucessor

        # Passa as referências dos widgets de antecessor e sucessor para o campo central
        self.central.set_valores(self.antecessor, self.sucessor)

        # Organiza os widgets na janela principal usando grid em uma única linha
        self.antecessor.grid(row=0, column=0)
        self.central.grid(row=0, column=1)
        self.sucessor.grid(row=0, column=2)

        # Inicia a atualização automática dos valores de antecessor e sucessor
        self.central.atualizar_automaticamente()

# Bloco para executar o programa somente se for o arquivo principal
if __name__ == "__main__":
    root = tk.Tk()          # Cria a janela principal do Tkinter
    app = App(root)         # Cria uma instância da aplicação
    root.mainloop()         # Inicia o loop principal do Tkinter (exibe a janela e aguarda eventos)
