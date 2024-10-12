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
            # Verifica se a cor do pixel é preta
            if (r, g, b) == (0, 0, 0):  # Verifica se o pixel é preto
                # Mover o mouse para a posição correta e desenhar um pixel
                pyautogui.moveTo(x + 200, y + 200)  # Ajuste a posição conforme necessário
                
                # Desenha um pixel
                pyautogui.mouseDown()
                pyautogui.move(1, 0)  # Move para a direita para desenhar um pixel
                pyautogui.mouseUp()
                time.sleep(0.01)  # Pequena pausa para controlar a velocidade do desenho

# Caminho da imagem que você deseja escanear
caminho_da_foto = 'coelho.jpg'  # Substitua pelo caminho da sua imagem

# Escanear e desenhar
imagem = escanear_foto(caminho_da_foto)
desenhar_no_paint(imagem)
