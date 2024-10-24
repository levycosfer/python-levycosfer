import segno
from segno import helpers

def link():
    compart = input("O que você compartilha seu QR Code: ")
    qrcode = segno.make_qr(compart)
    qrcode.save('QR-CODE.png', scale=30)

def wifi():
    ssid = input("Nome do Wifi SSID: ")
    password = input("Senha: ")
    security = input("Segurança: ")
    qrcode = helpers.make_wifi(ssid, password, security)
    qrcode.designator
    '3-M'
    qrcode.save('wifi-access.png', scale=10)

def escolhaqrcode():
    print("Escolha a opção para gerar QR Code")
    print("1. Link ou Palavra")
    print("2. Wifi")
    escolha=input("Digite a opção: ")
    if escolha=='1':
        link()
    elif escolha=='2':
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
#video.save('Video.png', dark="yellow", light="#323524", scale=5)