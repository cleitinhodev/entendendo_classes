#  Crie um programa que leia dois números e mostre a soma entre eles.

# Importa o módulo principal do tkinter
import tkinter as tk
# Importa os widgets mais modernos do tkinter (ttk)
from tkinter import ttk
# Importa o módulo de fontes para estilizar textos
from tkinter import font


# Define a classe Emissor, responsável pela entrada dos números e o botão de cálculo
class Emissor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)  # Inicializa o Frame pai
        self.receptor = None  # Variável que vai receber a referência ao receptor

        # Campos de entrada para os dois valores
        self.caixa_valor_a = ttk.Entry(self)
        self.caixa_valor_b = ttk.Entry(self)

        # Rótulos visuais "+" e "=" para melhorar o layout
        self.label_de_soma = tk.Label(self, text='+')
        self.label_de_igual = tk.Label(self, text='=')

        # Botão que calcula o resultado
        self.botao_de_resultado = ttk.Button(self, text='Ver Resultado', command=self.calcular_valores)

        # Organiza os widgets na tela usando grid (em linha)
        self.caixa_valor_a.grid(row=0, column=0, padx=10, pady=5)
        self.label_de_soma.grid(row=0, column=1, padx=10, pady=5)
        self.caixa_valor_b.grid(row=0, column=2, padx=10, pady=5)
        self.label_de_igual.grid(row=0, column=3, padx=10, pady=5)
        self.botao_de_resultado.grid(row=0, column=4, padx=10, pady=5)

    # Função que define o receptor (para onde será enviada a resposta)
    def set_receptor(self, receptor):
        self.receptor = receptor

    # Função que é chamada ao clicar no botão de calcular
    def calcular_valores(self):
        try:
            # Verifica se algum dos campos está vazio
            if not self.caixa_valor_a.get().strip() or not self.caixa_valor_b.get().strip():
                self.receptor.apresentar_resultado('Preencha os dois campos!')
                return

            # Tenta converter os valores digitados em float
            valor_a = float(self.caixa_valor_a.get())
            valor_b = float(self.caixa_valor_b.get())

            # Realiza a soma
            resultado = valor_a + valor_b

            # Envia o resultado para o receptor
            self.receptor.apresentar_resultado(resultado)

        except ValueError:
            # Caso os valores não possam ser convertidos para número
            self.receptor.apresentar_resultado('Digite apenas valores válidos (1, 20, 4.5...).')
        except AttributeError:
            # Caso o receptor não esteja configurado corretamente
            print("Erro: Receptor não está configurado corretamente.")
        except TypeError:
            # Caso ocorra um erro de tipo inesperado
            print("Erro de tipo inesperado.")


# Define a classe Receptor, responsável por exibir o resultado
class Receptor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)  # Inicializa o Frame pai
        self.emissor = None  # Referência futura ao emissor

        # Define uma borda ao redor do frame
        self['bd'] = 2
        self['relief'] = 'solid'

        # Cria uma fonte personalizada para o texto de exibição
        self.fonte = font.Font(family='Arial', size=10, weight="bold")

        # Label que mostra o resultado ou mensagens de erro
        self.display_de_soma = tk.Label(self,
                                        text='Digite dois valores...',
                                        width=60, height=3,
                                        font=self.fonte)
        self.display_de_soma.pack(padx=10, pady=5)  # Posiciona o label

    # Define o emissor (caso você queira usar a referência depois)
    def set_emissor(self, emissor):
        self.emissor = emissor

    # Função para atualizar o texto do display
    def apresentar_resultado(self, mensagem):
        if isinstance(mensagem, (int, float)):
            # Se a mensagem for um número, mostra como resultado em preto
            self.display_de_soma.config(text=f'Resultado: {mensagem}', fg='black')
        else:
            # Se a mensagem for uma string (mensagem de erro), mostra em vermelho
            self.display_de_soma.config(text=mensagem, fg='red')


# Classe principal da aplicação, que junta emissor e receptor
class App:
    def __init__(self, master):
        self.root = master  # Janela principal
        self.root.title('Soma Números')  # Título da janela

        # Cria instâncias do receptor e do emissor
        self.receptor = Receptor(self.root)
        self.emissor = Emissor(self.root)

        # Liga o receptor ao emissor e vice-versa
        self.receptor.set_emissor(self.emissor)
        self.emissor.set_receptor(self.receptor)

        # Posiciona os frames na tela
        self.receptor.pack(pady=5)
        self.emissor.pack(pady=5)


# Bloco principal que inicia o programa
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = App(root)  # Inicia o app com a janela
    root.mainloop()  # Mantém a janela aberta (loop principal do tkinter)
