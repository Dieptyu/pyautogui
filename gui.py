import time
import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(1328, 1409)
time.sleep(2)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(899, 407)
time.sleep(2)
pyautogui.write('cai coor center em lam khong duoc nen em lam nhu ri cung duoc', interval=0.25)
pyautogui.click(995, 708)

