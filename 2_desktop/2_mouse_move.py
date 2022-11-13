import pyautogui

# 절대 좌표
pyautogui.moveTo(-200, 1030) # 지정한 위치로 마우스를 이동
pyautogui.moveTo(100, 980, duration=0.5) # 0.5초 동안 이동

# 상대좌표 (현재 커서의 위치로부터)
pyautogui.move(100, -100, duration=0.5)

print(pyautogui.position()) # 마우스 좌표