import pyautogui


pyautogui.click(x=-1839, y=124, duration=0.5) # mdown과 mup의 조합임
pyautogui.mouseDown()   #
pyautogui.mouseUp()     # 드래그할때 활용 가능
# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 더블클릭과 같음

pyautogui.rightClick(x=-1639, y=124, duration=0.5) # 우클릭
# pyautogui.middleClick() # 휠 클릭
# pyautogui.drag(100, 0) # 드래그, 창 잡고 이동 가능, .move처럼 상대이동
#pyautogui.dragTo() # 절대 좌표로 이동

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤