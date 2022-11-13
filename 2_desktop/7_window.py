import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
print(fw.title) # 창의 제목 정보
print(fw.size) # 창의 크기 정보
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표

for w in pyautogui.getAllWindows():
    print(w) # 모든 창

print("---------------")
# 키워드가 포함된 창만 get
for w in pyautogui.getWindowsWithTitle("wh"):
    print(w) # 모든 창
    pyautogui.sleep(0.2)
    # w.activate() # 활성화 (맨 앞으로 가져오기)

    if w.isMaximized == False: # 현재 최대화가 되지 않았다면
        w.maximize() # 최대화
    pyautogui.sleep(0.3)
    if w.isMinimized == False: # 현재 최소화가 되지 않았다면
        w.minimize() # 최소화

    # w.close() # 창 닫기