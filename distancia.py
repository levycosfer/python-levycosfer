import math

# Recebe as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcula a distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verifica se a distância é maior ou igual a 10 ou menor
if distancia >= 10:
    print("longe")
else:
    print("perto")