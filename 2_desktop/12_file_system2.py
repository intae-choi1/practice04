import os
import fnmatch
# file name match
from pprint import pprint
import re

def sort_key(x):
    pattern = "\d+_\w*\.py"
    p = re.compile(pattern)
    m = p.search(x)
    num = m.group().split("_")[0]
    # num = x.split("\\")[-1].split("_")[0] 
    return int(num)


pattern = "*.py" 
result = []
for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
            result.append(os.path.join(root, name))

pprint(result)
print()

result.sort(key=sort_key)

pprint(result)