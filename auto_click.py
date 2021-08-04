import pyautogui
import keyboard
import threading


def stop():
    while True:
        pyautogui.tripleClick()
        if keyboard.is_pressed('s'):
            break

def play():
    while True:
        if keyboard.is_pressed('p'):
            stop()

threading.Thread(target=play())
threading.Thread(target=stop())
