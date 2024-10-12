# Programa para calcular o fatorial de um número natural

n = int(input("Digite o valor de n: "))

# Inicializa o valor do fatorial como 1
fatorial = 1

# Calcula o fatorial de n
for i in range(1, n + 1):
    fatorial *= i

# Exibe o resultado
print(fatorial)