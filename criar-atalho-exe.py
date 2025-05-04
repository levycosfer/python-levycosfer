import os
import win32com.client

def create_shortcut():
    # Caminho do executável
    exe_path = os.path.abspath("dist\gerator-qrcode.exe")
    
    # Caminho para criar o atalho (na área de trabalho)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    shortcut_path = os.path.join(desktop, "QR Code Generator.lnk")
    
    # Criando o atalho
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.IconLocation = exe_path  # Define o ícone como o próprio executável
    shortcut.save()

create_shortcut()