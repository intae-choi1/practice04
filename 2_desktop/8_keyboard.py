import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()


pyautogui.write("12345")
pyautogui.write("hi hi", interval=0.3) # 입력 시간 간격 

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"])
pyautogui.write("enter") # enter가 입력됨
pyautogui.write(["enter"]) # enter key를 침

pyautogui.keyDown("shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# pyautogui.hotkey("ctrl", "alt", "shift", "a") # Ctrl Alt Shift A 누르고,  역순으로 뗌
pyautogui.hotkey("ctrl", "a")

# 한글은 입력이 안되는데 해결 법 (클립보드에 넣고 붙여넣기)
# pip install pyperclip
# import pyperclip
# pyperclip.copy("한글한글") # 한글한글을 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") #한글 붙여넣기