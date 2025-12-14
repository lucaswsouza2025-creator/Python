# Definindo a variável utilizada
print('Olá, temos três jogos digitais disponíveis!')

jogos = input(
    'Escolha um deles para saber as informações '
    '(batman arkhan city, spider-man, guitar hero): ').strip().lower()
# Lembre-se o strip serve para remover os espaços extras, e o lower converte todas as letras para minúsculo

# Informando as condições válidas
if jogos == 'batman arkhan city':
    preco = 80.00
    onde = 'Xbox 360 e Playstation 3'
    jogador = '1 jogador'

elif jogos == 'spider-man':
    preco = 90.00
    onde = 'Exclusivo do Playstation 4'
    jogador = '1 jogador'

elif jogos == 'guitar hero':
    preco = 50.00
    onde = 'Xbox 360 e Playstation 3'
    jogador = '2 jogadores'

# Condição inválida
# Lembre-se o exit deve estar apenas dentro do else!
else:
    print('Essa informação é inválida. Por favor, escolha uma das opções de jogo para prosseguir!')
    exit()

# Exibindo os dados do jogo escolhido
print(f'O preço do jogo escolhido é R$ {preco}')
print(f'Está disponível para {onde}')
print(f'Pode ser jogado no modo offline por no máximo {jogador}')
