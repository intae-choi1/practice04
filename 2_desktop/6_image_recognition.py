import pyautogui
import time
import sys
# 화면에서 파일의 그림을 찾아서 반환
file_menu = pyautogui.locateOnScreen("img/file_menu.png")

print(file_menu)

pyautogui.click(file_menu)

# 여러개를 이터레이터로 반환
# file_menus = pyautogui.locateAllOnScreen("img/file_menu.png")



# 속도 개선
# 1. GrayScale, 정확도가 떨어질 수 있음
file_menu = pyautogui.locateOnScreen("img/file_menu.png", grayscale=True)

# 2. 찾을 범위 지정, xy부터 wh 범위까지
x = 1400
y = 600
width = 520 
height = 480
file_menu = pyautogui.locateOnScreen("img/file_menu.png", region=(x, y, width, height))

# 3. 정확도 조정, 1%만 일치해도 찾기 (opencv-python 설치 필요)
file_menu = pyautogui.locateOnScreen("img/file_menu.png", confidence=0.01)
pyautogui.moveTo(file_menu)
####



# 찾을 대상이 바로 나오는게 아닐 경우
# 1. 계속 기다리기
# while file_menu is None:
#     file_menu = pyautogui.locateOnScreen("img/file_menu.png", confidence=0.01)
# pyautogui.moveTo(file_menu)


# 2. 일정 시간동안 기다리기 (timeout)
timeout = 10
start = time.time()
file_menu = None
while file_menu is None:
    file_menu = pyautogui.locateOnScreen("img/file_menu.png", confidence=0.01)

    end = time.time()
    if end - start > timeout:
        print("시간종료")
        sys.exit()
        
pyautogui.moveTo(file_menu)