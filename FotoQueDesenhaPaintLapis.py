import cv2
import numpy as np
import pyautogui
import time
from PIL import Image

# Função para escanear a foto
def escanear_foto(caminho_foto):
    # Lê a imagem usando OpenCV
    img = cv2.imread(caminho_foto)
    
    # Converte a imagem para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    return img_rgb

# Função para desenhar a imagem no Paint
def desenhar_no_paint(imagem):
    # Abre o Paint (assegure-se de que o Paint está instalado e acessível)
    pyautogui.hotkey('win', 'r')  # Abre a janela de execução
    time.sleep(1)
    pyautogui.write('mspaint')  # Escreve "mspaint" para abrir o Paint
    pyautogui.press('enter')  # Pressiona Enter
    time.sleep(3)  # Espera o Paint abrir

    # Redimensiona a imagem para caber na tela do Paint
    imagem = Image.fromarray(imagem)
    imagem = imagem.resize((800, 600))  # Ajuste o tamanho conforme necessário
    imagem.show()  # Mostra a imagem para verificar

    # Desenha a imagem no Paint
    # O Paint deve estar em primeiro plano
    pyautogui.moveTo(200, 200)  # Move o mouse para a posição inicial no Paint
    pyautogui.click()  # Clica para garantir que o Paint está ativo
    time.sleep(1)  # Aguarda um momento para estabilizar o mouse

    # Usar a função de desenho do Paint
    width, height = imagem.size

    # Mover-se para a posição inicial
    for y in range(height):
        for x in range(width):
            r, g, b = imagem.getpixel((x, y))
            # Mover o mouse para a posição correta e desenhar um pixel
            pyautogui.moveTo(x + 200, y + 200)  # Ajuste a posição conforme necessário
            
            # Definir a cor atual do lápis
            if (r, g, b) != (255, 255, 255):  # Verifica se o pixel não é branco
                # Mudar a cor do lápis (pode precisar ajustar a posição do mouse)
                pyautogui.click(x=10, y=10)  # Clica em uma posição do Paint para abrir a paleta de cores
                pyautogui.moveTo(10, 10)  # Ajustar conforme a paleta de cores
                pyautogui.mouseDown()
                time.sleep(0.01)  # Espera um pouco para garantir que a cor foi escolhida
                pyautogui.mouseUp()

            # Desenha um pixel (aqui você pode usar um retângulo maior para aumentar a velocidade)
            pyautogui.mouseDown()
            pyautogui.move(1, 0)  # Move para a direita para desenhar um pixel
            pyautogui.move(0, 1)  # Move para baixo para desenhar um pixel
            pyautogui.mouseUp()

# Caminho da imagem que você deseja escanear
caminho_da_foto = 'pequeno.jpg'  # Substitua pelo caminho da sua imagem

# Escanear e desenhar
imagem = escanear_foto(caminho_da_foto)
desenhar_no_paint(imagem)
