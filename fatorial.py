def fatorial(n):
    fat = 1  # Inicializa a variável fat
    while n > 1:
        fat = fat * n  # Corrige a atribuição
        n = n - 1
    return fat  # Corrige a sintaxe

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if fatorial(5) == 120:  # Corrigido o valor esperado
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

# Chama a função de teste
testa_fatorial()
