
import re
import glob

txt = "hogehoge[abccbbss, bccc, [caaa, caaa], abb,]"

def matchlastComma(txt):
    pattern = r"(.*),"
    m = re.findall(pattern, txt, flags=(re.MULTILINE | re.DOTALL))
    if len(m) == 0:
        return txt
    return(m[0] + "]")

paths = glob.glob("./*.json")

for path in paths:
    fileText = ""
    with open(path, mode="r") as f:
        fileText = f.read()
        print(matchlastComma(fileText))
    with open(path, mode="w") as f:
        f.write(matchlastComma(fileText))





