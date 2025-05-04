def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(n):
    contagem_primos = 0
    for i in range(2, n + 1):
        if e_primo(i):
            contagem_primos += 1
    return contagem_primos

print(n_primos(2))
print(n_primos(4))   
print(n_primos(121))