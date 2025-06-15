# Crie um programa que escreva "Olá Mundo" na tela:

# Importa o módulo tkinter com o apelido tk (usado para criar interfaces gráficas)
import tkinter as tk
# Importa o módulo ttk, que fornece widgets com estilos mais modernos (botões, caixas, etc.)
from tkinter import ttk


# Classe que representa uma interface com texto, herda de tk.Frame
class InterfaceDeTexto(tk.Frame):
    def __init__(self, master):
        # Inicializa o frame base da classe
        super().__init__(master)

        # Define a cor de fundo como preta
        self['bg'] = '#000000'
        # Define uma borda de 2 pixels
        self['bd'] = 2
        # Define o estilo da borda como sólida
        self['relief'] = 'solid'
        # Define a largura do frame
        self['width'] = 400
        # Define a altura do frame
        self['height'] = 150
        # Impede que o frame se redimensione com base no conteúdo interno
        self.pack_propagate(False)

        # Cria um rótulo (label) com o texto inicial e estilo visual
        self.label_de_texto = tk.Label(
            self,  # O parent é o próprio frame
            text='Diga oi ao mundo!',
            font=('Arial', 20),        # Fonte e tamanho
            fg='#00ff0c',              # Cor da fonte (verde neon)
            background='#000000'       # Cor de fundo igual ao frame
        )
        # Posiciona o label no centro do frame, permitindo expansão
        self.label_de_texto.pack(expand=True)

    # Método que permite alterar o texto do label dinamicamente
    def mudar_texto(self, nova_mensagem):
        self.label_de_texto.configure(text=nova_mensagem)


# Classe principal da aplicação
class App:
    def __init__(self, master):
        # Armazena a janela principal
        self.root = master
        # Define o título da janela
        self.root.title('Diga - Olá Mundo!')
        # Define o tamanho fixo da janela
        self.root.geometry('420x220')
        # Define a cor de fundo da janela principal
        self.root['bg'] = '#703c88'
        # Configura a coluna 0 para expandir automaticamente com o conteúdo
        self.root.grid_columnconfigure(0, weight=1)

        # Cria a área de texto personalizada (frame com rótulo)
        self.interface_de_texto = InterfaceDeTexto(self.root)

        # Cria uma caixa de entrada de texto
        self.caixa_de_texto = ttk.Entry(self.root)
        # Insere um texto inicial na caixa de entrada
        self.caixa_de_texto.insert(0, "Olá Mundo")
        # Coloca o foco do cursor na caixa de texto automaticamente
        self.caixa_de_texto.focus()

        # Cria um botão com o texto "Enviar" que chama a função enviar_texto
        self.botao_de_oi = ttk.Button(self.root, text='Enviar', command=self.enviar_texto)

        # Posiciona o frame com o texto na linha 0, ocupando 2 colunas, com espaçamento
        self.interface_de_texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # Posiciona a caixa de texto na linha 1, coluna 0, com espaçamento e expansão horizontal
        self.caixa_de_texto.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        # Posiciona o botão na linha 1, coluna 1
        self.botao_de_oi.grid(row=1, column=1, padx=10, pady=10)

    # Função que altera o texto do label ao clicar no botão
    def enviar_texto(self):
        # Obtém o texto digitado e envia para o método que altera o rótulo
        self.interface_de_texto.mudar_texto(self.caixa_de_texto.get())


# Cria a janela principal da aplicação
root = tk.Tk()
# Inicializa a aplicação com a janela principal
app = App(root)
# Inicia o loop principal do Tkinter (janela interativa)
root.mainloop()
