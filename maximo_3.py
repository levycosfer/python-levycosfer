def maximo(a, b, c):
    maior = a  # Assume que o primeiro é o maior inicialmente
    if b > maior:
        maior = b  # Atualiza se o segundo é maior
    if c > maior:
        maior = c  # Atualiza se o terceiro é maior
    return maior
