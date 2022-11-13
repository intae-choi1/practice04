import pyautogui

pyautogui.countdown(1) # 3초를 세줌
print("시작")

# message, title
rslt = pyautogui.alert("자동화 실패", "경고") # 확인 버튼만 있음
print(rslt)

rslt = pyautogui.confirm("계속할래?", "확인ㅇ") # 확인, 취소 있음
print(rslt)

rslt = pyautogui.prompt("\이름 뭐로할래?", "입력") # 입력받음
print(rslt) # 취소누르면 None

rslt = pyautogui.password("암호를 입렿가세요", "입력") # 입력받음
print(rslt) # 취소누르면 None



