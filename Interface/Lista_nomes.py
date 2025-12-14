import tkinter as tk

# Dicionário para armazenar os nomes com uma chave única
clientes = {}
id_cliente = 1  # Contador para gerar uma chave única para cada cliente

# Função para adicionar o dado (nome) ao dicionário
def adicionar_dado():
    global id_cliente  # Usamos a variável global para controlar a chave única
    nome = entrada_nome.get()
    if nome:  # Verifica se o nome não está vazio
        
        # Adiciona o nome ao dicionário com a chave única
        clientes[id_cliente] = nome
        
        # Atualiza a lista de nomes na interface
        lista_nomes.insert(tk.END, nome)  # Adiciona o nome na Listbox
        id_cliente += 1  # Incrementa a chave para o próximo cliente
        entrada_nome.delete(0, tk.END)  # Limpa o campo de entrada
        
        rotulo_nome_adicionado.config(text=f"Nome '{nome}' adicionado com sucesso.")
    else:
        rotulo_nome_adicionado.config(text='Nome vazio não pode ser adicionado.')  # Mensagem de erro

# Função para fechar a aplicação
def sair():
    janela.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title('Formulário de Cadastro')
janela.geometry('800x600')  # Define o tamanho inicial da janela

# Frame para o cabeçalho
frame_cabecalho = tk.Frame(janela)
frame_cabecalho.pack(pady=10)

rotulo_boas_vindas = tk.Label(frame_cabecalho, text='Bem Vindo ao Sistema XYZ', font=('Arial', 16))
rotulo_boas_vindas.pack()

# Frame para entrada de dados
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

rotulo_nome = tk.Label(frame_entrada, text='Nome:')
rotulo_nome.pack(side=tk.LEFT, padx=5)

entrada_nome = tk.Entry(frame_entrada, width=30)
entrada_nome.pack(side=tk.LEFT, padx=5)

# Botão 'Adicionar'
botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar_dado)
botao_adicionar.pack(pady=10)

# Rótulo para mensagens de status
rotulo_nome_adicionado = tk.Label(janela, text='Nome Adicionado: Nenhum', fg='green')
rotulo_nome_adicionado.pack(pady=5)

# Frame para a lista de nomes
frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10)

rotulo_lista = tk.Label(frame_lista, text='Lista de Nomes:')
rotulo_lista.pack()

lista_nomes = tk.Listbox(frame_lista, height=10, width=40)
lista_nomes.pack()

# Botão 'Sair'
botao_sair = tk.Button(janela, text='Sair', command=sair, bg='red', fg='white')
botao_sair.pack(pady=10)

# Iniciar o loop principal
janela.mainloop()
