import pyautogui
import pyperclip
import time

pyautogui. PAUSE = 0.8

#entrar numa nova guia

pyautogui.hotkey("ctrl","t")

time.sleep(0.5)
desimpedidos

#escrever o link do youtube

pyperclip.copy("https://www.youtube.com/")

pyautogui.hotkey("ctrl","v")

time.sleep(0.5)

#dar go

pyautogui.press("enter")

#escrever o canal desimpedidos

pyautogui.click(x=570, y=100)

pyperclip.copy("desimpedidos")

pyautogui.hotkey("ctrl","v")

#clicar para pesquisar

time.sleep(0.8)

pyautogui.press("enter")

#clicar no video

pyautogui.click(x=705, y=210, clicks=2)

time.sleep(1.6)

#aumentar a tela

pyautogui.click(x=851, y=610)