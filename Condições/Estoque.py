# Revisar os códigos
# Adicionar estoque
estoque = {}

while True:
    print('MENU DE OPÇÃO:')
    print('1 - Adicionar Estoque')
    print('2 - Consultar Estoque')
    print('3 - Remover Estoque')
    print('4 - Sair')
    
    escolha = input('Escolha uma opção: ')
    
    # Comandos para cada opção escolhida
    if escolha == '1':
        nome_produto = input('\nDigite o nome do produto: ').strip().lower() # Converter para minúsculo
        
        try:
            quantidade = int(input('Digite a quantidade: '))
            
            if quantidade <= 0: # Validação para quantidade maior que zero
                print('A quantidade deve ser maior que zero. Tente novamente.')
            else:
                if nome_produto in estoque:
                    estoque[nome_produto] += quantidade
                else:
                    estoque[nome_produto] = quantidade
                print(f'{quantidade} unidade(s) de {nome_produto} adicionadas ao estoque.')
        except ValueError:
            print('Quantidade inválida. Tente novamente.')
            
# Produtos no estoque
    if escolha == '2':
        if not estoque:                
            