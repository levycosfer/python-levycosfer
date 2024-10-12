# Programa para verificar se um número possui dígitos adjacentes iguais

# Recebe o número inteiro na entrada
numero = input("Digite um número inteiro: ")

# Inicializa a variável para verificar dígitos adjacentes
tem_digito_adjacente = False

# Percorre os dígitos do número
for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:  # Verifica se o dígito atual é igual ao próximo
        tem_digito_adjacente = True
        break

# Imprime o resultado
if tem_digito_adjacente:
    print("sim")
else:
    print("não")
