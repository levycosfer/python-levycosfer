import math

# Função para calcular as raízes da equação do segundo grau
def calcular_raizes(a, b, c):
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c

    # Verifica as condições das raízes
    if delta < 0:
        print("esta equação não possui raízes reais")
    elif delta == 0:
        # Uma raiz real (raiz dupla)
        x = -b / (2*a)
        print(f"a raiz dupla desta equação é {x}")
    else:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        
        # Exibe as raízes em ordem crescente
        if x1 < x2:
            print(f"as raízes da equação são {x1} e {x2}")
        else:
            print(f"as raízes da equação são {x2} e {x1}")

# Recebe os parâmetros da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula e imprime as raízes da equação
calcular_raizes(a, b, c)
