import os
import time
import datetime

# print(os.getcwd()) # current working directory

# os.chdir("1_excel")
# print(os.getcwd())

# os.chdir("..") # 상위 디렉터리
# print(os.getcwd())

# os.chdir("../..")
# print(os.getcwd())

# os.chdir("c:/") # 절대 경로
# print(os.getcwd())


# 파일 경로
file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대경로
# 파일 경로에서 폴더 정보 가져오기
# r"" 은 escape 문자를 무시하고 있는 그대로 처리해줌
print(os.path.dirname(r"C:\Users\MZC01-INTAECHOI\Desktop\personal_WorkSpace\PythonWorkSpace\rpa_basic\2_desktop\my_file.txt"))

# 파일 정보 가져오기
# 파일의 생성 날짜
ctime = os.path.getctime("../tmp.py") # get create time
print(ctime)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

# 수정 날짜 
mtime = os.path.getmtime("../tmp.py")
print(mtime)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# 마지막 접근 날짜
atime = os.path.getatime("../tmp.py")
print(atime)
print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일 크기
size = os.path.getsize("../tmp.py")
print(size, "bytes")


# 파일 목록
print(os.listdir()) # 모든 폴더, 파일 정보 가져오기 (cwd 기준)
print(os.listdir("..")) # 주어진 경로 아래서 가져오기

print()
# 하위 경로까지 다 가져오기
result = os.walk("../1_excel") # generator 반환
for root, dirs, files in result:
    # root: 상위 dir, dirs: root에 포함된 디렉터리들, files: root에 포함된 파일들
    print(root, dirs, files)
print()

# 파일 찾기
name = "11_file_system.py"
result = []
for root, dirs, files in os.walk(os.getcwd()):
    if name in files:
        result.append(os.path.join(root, name))
print(result)
print("ddddddd")

base = os.path.dirname(os.path.realpath(__file__))
print(base)
print(os.path.dirname(base))
print(os.path.dirname(os.path.dirname(base)))


result = os.walk(os.path.dirname("../")) # generator 반환
for root, dirs, files in result:
    # root: 상위 dir, dirs: root에 포함된 디렉터리들, files: root에 포함된 파일들
    print(root, dirs, files)