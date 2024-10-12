def vogal(caractere):
    """Retorna True se o caractere for uma vogal e False se for uma consoante."""
    # Verifica se o caractere é uma vogal
    return caractere.lower() in 'aeiou'

# Exemplos de execução
x=input("Escreve: ") 
print(vogal(x))
