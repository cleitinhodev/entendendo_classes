# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

import tkinter as tk               # Importa o módulo principal do Tkinter (interface gráfica)
from tkinter import ttk           # Importa a parte "moderna" do Tkinter (temas, widgets mais bonitos)


# Classe responsável por exibir os resultados da análise do texto
class Vizualizando(tk.Frame):
    def __init__(self, master):
        super().__init__(master)  # Inicializa o Frame (janela interna)

        self.area_de_envio = None  # Vai armazenar a referência à outra parte da interface

        # Cria a tabela com duas colunas e sem coluna de árvore (somente os cabeçalhos)
        self.tabela = ttk.Treeview(self, columns=("Tipo", "Confirmação"),
                                   show="headings")

        # Define o nome dos cabeçalhos das colunas
        self.tabela.heading("Tipo", text="Tipo")
        self.tabela.heading("Confirmação", text="Confirmação")

        # Define o alinhamento das colunas
        self.tabela.column("Tipo", anchor="w")        # Alinha à esquerda
        self.tabela.column("Confirmação", anchor="center")  # Centraliza

        # Adiciona as linhas fixas à tabela (uma para cada informação que será analisada)
        # E armazena os IDs das linhas em variáveis para poder atualizá-las depois
        self.tipo = self.tabela.insert("", "end", values=("Tipo Primitivo", ''))
        self.somente_espacos = self.tabela.insert("", "end", values=("Só tem espaços?", ''))
        self.numerico = self.tabela.insert("", "end", values=("É numérico?", ''))
        self.alfabetico = self.tabela.insert("", "end", values=("É alfabético?", ''))
        self.alfanumerico = self.tabela.insert("", "end", values=("É alfanumérico?", ''))
        self.maiusculas = self.tabela.insert("", "end", values=("Está em maiúsculas?", ''))
        self.minusculas = self.tabela.insert("", "end", values=("Está em minúsculas?", ''))
        self.captalizada = self.tabela.insert("", "end", values=("Está captalizada?", ''))

        self.tabela.pack()  # Exibe a tabela na tela

    # Método para conectar este frame ao componente que envia os dados
    def set_area_de_envio(self, area_de_envio):
        self.area_de_envio = area_de_envio

    # Método que recebe o valor digitado e atualiza a tabela com as análises
    def processar_valor(self, valor):
        # Analisa cada característica do valor digitado
        tipo = str(type(valor))                  # Tipo primitivo
        somente_espacos = str(valor.isspace())   # Só espaços?
        numerico = str(valor.isnumeric())        # É numérico?
        alfabetico = str(valor.isalpha())        # Só letras?
        alfanumerico = str(valor.isalnum())      # Letras e números?
        maiusculas = str(valor.isupper())        # Está em maiúsculas?
        minusculas = str(valor.islower())        # Está em minúsculas?
        captalizado = str(valor.istitle())       # Primeira letra maiúscula em cada palavra?

        # Atualiza cada linha da tabela com os valores analisados
        self.tabela.item(self.tipo, values=("Tipo Primitivo", tipo))
        self.tabela.item(self.somente_espacos, values=("Só tem espaços?", somente_espacos))
        self.tabela.item(self.numerico, values=("É numérico?", numerico))
        self.tabela.item(self.alfabetico, values=("É alfabético?", alfabetico))
        self.tabela.item(self.alfanumerico, values=("É alfanumérico?", alfanumerico))
        self.tabela.item(self.maiusculas, values=("Está em maiúsculas?", maiusculas))
        self.tabela.item(self.minusculas, values=("Está em minúsculas?", minusculas))
        self.tabela.item(self.captalizada, values=("Está captalizada?", captalizado))


# Classe responsável por exibir a entrada de dados e o botão
class AreaDeEnvio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)        # Inicializa o frame
        self['bd'] = 1                  # Borda de 1 pixel
        self['relief'] = 'solid'       # Borda sólida (caixa com contorno)

        self.vizualizando = None        # Referência ao frame que mostra os dados

        # Caixa de texto onde o usuário digita o valor
        self.caixa_de_valor = ttk.Entry(self, width=40)

        # Botão que ao ser clicado chama o método enviar_valor
        self.botao_de_verificacao = ttk.Button(self, text='Identificar', command=self.enviar_valor)

        # Posiciona a entrada e o botão lado a lado com espaçamento
        self.caixa_de_valor.grid(row=0, column=0, padx=20, pady=10)
        self.botao_de_verificacao.grid(row=0, column=1, padx=20, pady=10)

    # Método que conecta esse frame ao que mostra os dados
    def set_vizualizando(self, vizualizando):
        self.vizualizando = vizualizando

    # Método que envia o valor digitado para ser analisado
    def enviar_valor(self):
        # Pega o texto da caixa de entrada e envia para o frame de visualização
        self.vizualizando.processar_valor(self.caixa_de_valor.get())


# Classe principal que monta toda a interface e conecta as partes
class App:
    def __init__(self, master):
        self.root = master  # Guarda a janela principal
        self.root.title('Tipo e Informações')

        # Cria os dois frames (visualização e envio)
        self.vizualizando = Vizualizando(self.root)
        self.area_de_envio = AreaDeEnvio(self.root)

        # Conecta um frame ao outro
        self.vizualizando.set_area_de_envio(self.area_de_envio)
        self.area_de_envio.set_vizualizando(self.vizualizando)

        # Exibe os frames na tela
        self.area_de_envio.pack(fill='both')
        self.vizualizando.pack()


# Código principal (só roda se for executado diretamente)
if __name__ == "__main__":
    root = tk.Tk()      # Cria a janela principal
    app = App(root)     # Inicia a aplicação
    root.mainloop()     # Mantém a janela aberta e rodando
