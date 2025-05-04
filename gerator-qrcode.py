import segno
from segno import helpers
import os
import sys

def get_desktop_directory():
    # Obtém o caminho da área de trabalho do usuário
    return os.path.join(os.path.expanduser("~"), "Desktop")

def link():
    compart = input("O que você compartilha seu QR Code: ")
    qrcode = segno.make_qr(compart)
    filename = os.path.join(get_desktop_directory(), 'QR-CODE.png')
    qrcode.save(filename, scale=30)
    print(f"QR Code salvo como '{filename}' na área de trabalho.")
    os.startfile(filename)  # Abre o arquivo automaticamente

def wifi():
    ssid = input("Nome do Wifi SSID: ")
    password = input("Senha: ")
    security = input("Segurança (ex: WPA, WPA2, etc.): ")
    qrcode = helpers.make_wifi(ssid, password, security)
    filename = os.path.join(get_desktop_directory(), 'wifi-access.png')
    qrcode.save(filename, scale=10)
    print(f"QR Code para Wi-Fi salvo como '{filename}' na área de trabalho.")
    os.startfile(filename)  # Abre o arquivo automaticamente

def escolhaqrcode():
    print("Escolha a opção para gerar QR Code")
    print("1. Link ou Palavra")
    print("2. Wifi")
    escolha = input("Digite a opção: ")
    if escolha == '1':
        link()
    elif escolha == '2':
        wifi()

escolhaqrcode()

#from segno import helpers

#qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
#qrcode.designator
#'3-M'
#qrcode.save('wifi-access.png', scale=10)

#import segno
#color amarelo
#video = segno.make('https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A')
#video.save('Video.png', dark="yellow", light="#323524", scale=5)1