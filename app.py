import pyautogui
import time


# Path of skip button
imagem = "files/pular.png"


# Inifite loop to verify screen image
while True:
    try:
        posicao = pyautogui.locateOnScreen(imagem, confidence=0.8)
        
        if posicao:
            print(f"Botão encontrado em {posicao}")
            
            pyautogui.click(pyautogui.center(posicao))
            
            time.sleep(2)
        else:
            print("...")
            
    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada, tentando novamente")
        
        time.sleep(1)