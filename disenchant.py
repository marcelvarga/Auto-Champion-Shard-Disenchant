import pyautogui
import time
import win32api
from pynput.mouse import Listener, Button
from collections import deque

isRunning = False
recordedMousePositions = deque(maxlen=3)
mousePositions = [[0, 0], [0, 0], [0, 0]]

def disenchant():
    # Move mouse to champion
    pyautogui.moveTo(mousePositions[0][0], mousePositions[0][1])
    pyautogui.click()
    time.sleep(0.5)

    # Move to disenchant into essence button
    pyautogui.moveTo(mousePositions[1][0], mousePositions[1][1])
    pyautogui.click()
    time.sleep(0.5)

    # Click disenchant button
    pyautogui.moveTo(mousePositions[2][0], mousePositions[2][1])
    pyautogui.click()
    time.sleep(1.6)

def on_click(x, y, button, pressed):
    # Store the last three clicks
    if pressed and button == Button.left:
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        recordedMousePositions.append((x, y))

# Record mouse clicks
listener = Listener(on_click=on_click)
listener.start()

while True:
    
    if win32api.GetAsyncKeyState(0x51) != 0:
        print("Exiting...")
        listener.stop()
        exit()
        

    if win32api.GetAsyncKeyState(0x53) != 0:
        if len(recordedMousePositions) < 3:
            print("Not enough clicks recorded")
            time.sleep(0.1)
            continue
        print("Starting...")

        listener.stop()
        isRunning = True
        mousePositions[0] = recordedMousePositions[0]
        mousePositions[1] = recordedMousePositions[1]
        mousePositions[2] = recordedMousePositions[2]

    if isRunning == True:
        disenchant()
