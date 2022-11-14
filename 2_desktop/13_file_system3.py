import os

print(os.path.isdir("img"))
print(os.path.isfile("img"))
print(os.path.isdir("../2_desktop"))

# 존재하는지 확인
if os.path.exists("../2_desktop"):
    print("존재")
else: print("없음")

# 파일 만들기
open("new_file.txt", "a").close()

# 바꿀 이름이 있으면 에러
os.rename("new_file.txt", "new_file_rename.txt")

# 지울 파일이 없으면 에러
os.remove("new_file_rename.txt")

# 폴더 만들기, 있으면 에러
try:
    os.mkdir("new_folder") # 절대 경로도 가능
except: pass

# 하위 폴더를 가지는 폴더 생성, 있으면 에러(옵션으로 무마)
os.makedirs("new_folder/a/b", exist_ok=True)

try:
    # 바꿀 이름이 있으면 에러
    os.rename("new_folder", "new_folder_rename")
except: pass

try:
    os.rmdir("new_folder_rename") # 폴더 안이 비었을때만 삭제 가능
except: pass

import shutil # shell utilites

shutil.rmtree("new_folder_rename") # 비어있지 않아도 삭제 가능