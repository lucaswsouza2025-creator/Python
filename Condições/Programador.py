# Identificando a linguagem o programador
# Determinando o espaço a ser preenchido, e convertendo as letras para minúsculo
print('Olá seja Bem-Vindo(a)!')
nivel = input('Por favor, digite o seu nível profissional entre programador (junior, senior ou expecialista): ').strip().lower()

# Condições Válidas
if nivel == 'junior':
    linguagens = 'Python, HTML e CSS'
    salario = 1800.00
    horario = '6 horas'

elif nivel == 'senior':
    linguagens = 'C++, JavaScript e C#'
    salario = 2300.00
    horario = '9 horas'

elif nivel == 'expecialista':
    linguagens = 'C++, SQL Server, Python, JavaScript, HTML e CSS'
    salario = 2800.00
    horario = '9 horas'

# Concição que vai dar erro
else:
    print('Informação Inválida. Por favor, digite algum nível correspondente!')
    exit() # Pedindo para o programa terminar a execução

# Mensagem final para o usuário
print(f'As linguagens que você vai utilizar é {linguagens}')
print(f'O seu salário vai ser de R$ {salario} Mensais')
print(f'O seu tempo diário de trabalho é de {horario}')