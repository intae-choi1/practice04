import os
import shutil

# 복사
shutil.copy("img/file_menu.png", "../1_excel") # 대상 경로에 같은 이름으로
shutil.copy("img/file_menu.png", "copyTo.png") # 지정된 경로에 지정된 이름으로

# 항상 대상 파일 명까지 들어가야됨
shutil.copyfile("img/file_menu.png", "copyTo2.png")

# copy2: 메타정보(생성 날짜 등)도 복사 (copy, copyfile은 안함), copy와 사용법은 같음
shutil.copy2("img/file_menu.png", "copy2.png")

# 폴더 복사
# shutil.copytree("img", "img2") # 안에거 까지 복사, target이 있으면 에러

# 폴더 이동
shutil.move("img2/c/d/b", "img2/d") # target에 이미 존재하면 에러, 없는 target으로 가면 rename 효과