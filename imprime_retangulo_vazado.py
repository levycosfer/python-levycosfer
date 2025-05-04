# Solicita ao usuário a largura e altura do retângulo
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Loop para cada linha (altura do retângulo)
for i in range(altura):
    # Verifica se é a primeira ou última linha
    if i == 0 or i == altura - 1:
        print("#" * largura)  # Imprime a linha inteira de '#'
    else:
        # Linhas internas com bordas
        print("#" + " " * (largura - 2) + "#")
