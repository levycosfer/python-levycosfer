def eh_primo(k):
    """Verifica se um número k é primo."""
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def maior_primo(n):
    """Retorna o maior número primo menor ou igual a n."""
    maior = None  # Inicializa a variável para armazenar o maior primo encontrado
    for num in range(2, n + 1):  # Percorre todos os números de 2 até n
        if eh_primo(num):
            maior = num  # Atualiza o maior primo encontrado
    return maior  # Retorna o maior primo encontrado

# Exemplos de execução
print(maior_primo(100))  # Saída: 97
print(maior_primo(7))    # Saída: 7
