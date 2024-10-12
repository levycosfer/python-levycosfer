# Recebe um número inteiro na entrada
num = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 e por 5
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)