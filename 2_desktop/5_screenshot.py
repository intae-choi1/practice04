import pyautogui

# 스크린 샷 찍기
img = pyautogui.screenshot()
img.save("scr.png")

# 해당 좌표 pixcel의 RGB
pixel = pyautogui.pixel(28, 18)
print(pixel)
