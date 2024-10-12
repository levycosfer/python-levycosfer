# Programa para imprimir os n primeiros números ímpares naturais

n = int(input("Digite o valor de n: "))

# Inicializa o contador de ímpares
impar = 1

# Loop para imprimir os n primeiros números ímpares
for i in range(n):
    print(impar)
    impar += 2  # Incrementa para o próximo número ímpar
