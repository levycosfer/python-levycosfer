# Recebe três números inteiros na entrada
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Verifica se estão em ordem crescente
if num1 < num2 < num3:
    print("crescente")
else:
    print("não está em ordem crescente")
