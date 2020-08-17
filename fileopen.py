import os

path = "./hogehoge.txt"

with open(path, mode='w') as f:
    f.write("a")

with open(path) as f:
    t = f.read()
    print(t)