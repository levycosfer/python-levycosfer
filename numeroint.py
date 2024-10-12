# Programa para calcular a soma dos dígitos de um número inteiro

# Recebe o número inteiro na entrada
numero = input("Digite um número inteiro: ")

# Inicializa a soma dos dígitos
soma = 0

# Percorre cada dígito do número
for digito in numero:
    soma += int(digito)  # Converte o dígito para inteiro e soma

# Exibe o resultado
print(soma)
