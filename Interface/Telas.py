import tkinter as tk

# Janela principal
janela = tk.Tk()
janela.title ('Olá seja bem vindo ao site!')

# Adicionar rótulo
titulo = tk.Label (janela, text = 'Para começar escolha as seguintes opções:')
titulo.pack()

# Adiciona um botão
def clique():
    print("Botão clicado!")
botao = tk.Button(janela, text="Clique Aqui", command=clique)
botao.pack()

# Inicia o loop principal da interface
janela.mainloop()


