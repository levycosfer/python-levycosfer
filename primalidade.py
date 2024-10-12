# Programa para verificar se um número inteiro positivo é primo

# Recebe o número inteiro positivo na entrada
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é menor que 2
if numero < 2:
    print("não primo")
else:
    # Inicializa a variável para verificar se é primo
    primo = True

    # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada de numero
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    # Imprime se o número é primo ou não
    if primo:
        print("primo")
    else:
        print("não primo")
