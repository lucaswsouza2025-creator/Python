# Tentando programar o mais simples possível, Operações básicas!
print('Calculo das operações básica de uma só vez são elas: adição, subtração, multiplicação e divisão!')
print('OBS: se for número decimal, por favor digite um ponto final e não vírgula!')

# Interação e variáveis
n1 = float(input('Por favor, digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2
subtrai = n1 - n2
multi = n1 * n2
dividi = n1 / n2

# Mostrando o resultando com todas as operações!
print('A soma entre os números {:.1f} e {:.1f} o resultado é {:.1f}'.format(n1, n2, soma))
print('O resultado da subtração é {:.1f}'.format(subtrai))
print('Da multilplicação é {:.1f}'.format(multi))
print('E da divisão é {:.1f}'.format(dividi))