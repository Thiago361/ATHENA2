import pyautogui
import time

def escutarMusica(musicaEscolhida):
    pyautogui.press("win")
    pyautogui.write("spotify")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "k")
    pyautogui.write(musicaEscolhida)
    time.sleep(1)
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("alt", "tab")