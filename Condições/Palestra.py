# Solicita ao usuário o nível de experiência
nivel = input("Por favor, digite o nível da sua experiência entre: (novato, experiente, especialista): ").strip().lower()

# Determina os recursos e tempo de palestra com base no nível
# Essa parte é opcional, o usuário é que vai escolher!
if nivel == 'novato':
    tempo = 30
    recursos = "lousa digital, caixa de som e microfone bluetooth"
    sala = 1
    
elif nivel == 'experiente':
    tempo = 45
    recursos = "projetor, microfone de lapela e acesso ao computador"
    sala = 2
    
elif nivel == 'especialista':
    tempo = 60
    recursos = "projetor 4K, microfone de lapela, sistema de videoconferência e acesso ao computador de alta performance"
    sala = 3
    
else:
    print("Nível de experiência inválido. Por favor, insira 'novato', 'experiente' ou 'especialista'.")
    exit()  # Encerra o programa se a entrada for inválida

# Exibe as informações
print(f"\nSeu tempo de palestra será de {tempo} minutos!")
print(f"Você terá acesso aos seguintes recursos: {recursos}.")
print(f"Sua sala será a número {sala}!")