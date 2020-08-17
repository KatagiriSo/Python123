import glob
import os
import re

paths = glob.glob("./*.*.json")

for path in paths:
    file = os.path.basename(path)

    pattern = r".*\.(.*\.json)"
    m = re.findall(pattern,file)
    os.rename(path, "./"+m[0])
    print(m)

