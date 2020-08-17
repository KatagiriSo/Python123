import re


while True:
    inp = str(input("input="))
    ans = re.sub("[0-9]","9",inp)
    print(ans)

