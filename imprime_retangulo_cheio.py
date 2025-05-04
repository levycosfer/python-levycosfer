# Solicita ao usuário a largura e altura do retângulo
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Loop externo para cada linha (altura do retângulo)
for i in range(altura):
    # Loop interno para cada coluna (largura do retângulo)
    for j in range(largura):
        print("#", end="")  # Imprime "#" na mesma linha
    print()  # Quebra de linha ao final de cada linha
