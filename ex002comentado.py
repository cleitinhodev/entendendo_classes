# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# Importa o módulo tkinter com alias 'tk' para usar a interface gráfica
import tkinter as tk
# Importa o módulo ttk (versão mais moderna dos widgets do tkinter)
from tkinter import ttk


# Classe responsável por mostrar a entrada de texto (nome) e o botão de envio
class DisplayDeEscrita(tk.Frame):
    def __init__(self, master, display_de_mensagem):
        # Inicializa a classe base (Frame)
        super().__init__(master)

        # Define uma borda e um estilo para o frame
        self['bd'] = 2
        self['relief'] = 'solid'   # Borda com estilo "sólido"
        self['width'] = 325        # Largura do frame
        self['height'] = 250       # Altura do frame

        # Impede que o frame se redimensione automaticamente com base no conteúdo
        self.pack_propagate(False)

        # Recebe o outro frame como argumento para poder enviar mensagens a ele
        self.display_de_mensagem = display_de_mensagem

        # Cria um rótulo com uma pergunta ao usuário
        self.texto_de_ajuda = tk.Label(self, text='Diga, qual é o seu nome?', font=('Calisto MT', 20))

        # Cria uma caixa de entrada (campo de texto)
        self.caixa_de_nome = ttk.Entry(self, width=40)

        # Cria um botão com o texto 'Enviar' que chama o método enviar_nome quando clicado
        self.botao_de_envio = ttk.Button(self, text='Enviar', command=self.enviar_nome)

        # Posiciona os widgets no frame com espaçamento vertical (pady)
        self.texto_de_ajuda.pack(pady=10, expand=True)
        self.caixa_de_nome.pack(pady=10, expand=True)
        self.botao_de_envio.pack(pady=10, expand=True)

    # Método que envia o texto digitado para o outro frame (DisplayDeMensagem)
    def enviar_nome(self):
        # Chama o método apresentar_nome passando o valor digitado na caixa de entrada
        self.display_de_mensagem.apresentar_nome(self.caixa_de_nome.get())


# Classe responsável por exibir a mensagem de boas-vindas
class DisplayDeMensagem(tk.Frame):
    def __init__(self, master):
        # Inicializa o frame base
        super().__init__(master)

        # Define aparência do frame
        self['bd'] = 2
        self['relief'] = 'solid'
        self['width'] = 175
        self['height'] = 250
        self['bg'] = '#000000'  # Cor de fundo preta

        # Impede redimensionamento automático do frame
        self.pack_propagate(False)

        # Cria um rótulo vazio onde a mensagem será exibida
        self.mensagem_de_boas_vindas = tk.Label(
            self,
            text='',
            font=('Arial', 14),
            fg='white',      # Cor da fonte
            bg='#000000'     # Cor de fundo do label igual ao frame
        )

        # Posiciona o label centralizado
        self.mensagem_de_boas_vindas.pack(expand=True)

    # Método chamado para exibir a mensagem com o nome da pessoa
    def apresentar_nome(self, novo_nome):
        nome = novo_nome
        if nome:
            # Caso o nome não esteja vazio, exibe a mensagem com o nome centralizado em 21 caracteres
            self.mensagem_de_boas_vindas.configure(text=f'  Seja Bem-vindo(a)!  \n{novo_nome:^21}')
        else:
            # Caso o nome esteja vazio, exibe a mensagem com "Desconhecido"
            self.mensagem_de_boas_vindas.configure(text=f'  Seja Bem-vindo(a)!  \n{"Desconhecido":^21}')


# Classe principal que organiza a interface
class Gerenciamento:
    def __init__(self, master):
        # Define a janela principal
        self.root = master
        self.root.title('Mensagem de Boas-Vindas')
        self.root.geometry('500x250')  # Tamanho da janela

        # Cria o frame que mostra a mensagem e o adiciona à grid (lado esquerdo)
        self.display_de_mensagem = DisplayDeMensagem(self.root)
        self.display_de_mensagem.grid(row=0, column=0)

        # Cria o frame com entrada de texto e botão, passando o frame da mensagem como referência
        self.display_de_escrita = DisplayDeEscrita(self.root, self.display_de_mensagem)
        self.display_de_escrita.grid(row=0, column=1)  # Adiciona ao lado direito


# Ponto de entrada do programa — executa o app apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    # Cria a janela principal do tkinter
    root = tk.Tk()

    # Instancia a classe de gerenciamento, que organiza tudo
    app = Gerenciamento(root)

    # Inicia o loop principal da interface gráfica
    root.mainloop()
