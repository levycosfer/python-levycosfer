import pyautogui
import time

# Função para registrar o clique inicial
def registrar_primeiro_clique():
    print("Posicione o cursor no local desejado e pressione ENTER para registrar a posição...")
    input("Pressione ENTER agora:")
    posicao = pyautogui.position()  # Captura a posição do cursor
    print(f"Posição registrada: {posicao}")
    return posicao

# Registrar a posição do primeiro clique
posicao_inicial = registrar_primeiro_clique()

# Contador para controlar as repetições
contador = 0

# Loop que repete 10 vezes
while contador < 10:
    print(f"Repetição número {contador + 1}")

    # Exemplo de ações
    pyautogui.click(x=1090, y=440)  # Clica em um ponto
    print("Clique realizado.")
    
    time.sleep(1)  # Aguarda 1 segundo

    pyautogui.scroll(-85)  # Rola para baixo
    print("Rolagem realizada.")
    
    time.sleep(1)  # Aguarda 1 segundo

    # Incrementa o contador
    contador += 1

print("Repetições concluídas.")

