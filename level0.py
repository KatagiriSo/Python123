# coding: utf-8
# コメントに日本語をつけるおまじない

# 主な参照先
# とほほ http://www.tohoho-web.com/python/index.html

# reduceはfunctoolsに移りました。
from functools import reduce


# インタプリタから読み込みたいならimport hello
# hello.add(3,4)とかできる。

print("Hello world!")

print(1+3)

a = 3;
b = 4;
c = a + b;

print(c);

#配列
months = ["Jan","Feb"];

print(months[0])

g = [1,2,3,4,5]
h = ["3",2]

for n in g:
    print(n)

k = g[1:3]#1から３番目
l = g[2:]#2番目から最後
m = g[0:5:2]#0番目から５番目まで2個とばし
o = g[-1]#最後の文字
o = g[-2]#最後から２番めの文字

for n in l:
    print(n)

print("最後から２番めの文字は")
print(o)

# インデントはブロックとみなされる。
if a == 3:
    print("a")
    print("b")

print ("c!")

# Pythonでは定数はサポートされないが大文字とかつかう。
A_SIZE = 3


k = [1,2]+[4,4]
l = len(k)
m = [[1,2],[3,3]]
p = (10,10)#タプルは要素を変更できない(代入できない)
q = list(p)#タプルからリスト
t = tuple([1,2]) #リストからタプル

dic = {"poi":3,"poipoi":4}
print(dic["poi"])
print(dic.items())
print(dic.keys())
print(dic.values())

#関数?
def d(x): return x*2

#map
x = map(d,[3,4,5])
print(list(x))

#ラムダ式で
y = map(lambda x: x*2, [1,2])
print(list(y))

#filterは真のものを取り出してくる。
def isodd(x):return x%2
print(list(filter(isodd, [1,2,3,4,5])))
print(list(filter(lambda x:x%2, [1,2,3,4,5])))

def add(x,y): return x+y
print(reduce(add,[1,2,3,4,5]))

#リスト内包表記
print([x*2 for x in [1,2,3]])
print([x*2 for x in [1,2,3] if x == 3])
print([(x,x*2) for x in [1,2,3]])
print([[x,x*2] for x in [1,2,3]])

print([x * y for x in [1,2] for y in [3,4]])

#集合
a = set([1,2,3,4,1,2,3,4])
print(a)

b = set([1,2,3]) - set([1,2])
c = set([1,2,3]) | set([2,3,4])
d = set([1,2]) & set([2,3])
e = set([1,2]) ^ set([2,3]) #これは何？1,3

print(e)

print(1 in [1,2,3]) #True

a = set([1,2,3])


if 3>2:
    print("3>2")
elif 5>2:
    print("5>2")
else:
    print("3<2")

n=0
while n<10:
    n+=1
    print(n)
else:
    print("おわた")

for k in {"key1":1, "key2":2}:
    print(k)

for n in range(3):
    print(n)

print("ループ")
for n in range(5):
    if n==2:
        continue
    print(n)
    if n==3:
        break

def add(x,y):
    print(x,y)
    return x+y

c = add(3,5)
print(c)

def func():
    return 3,"a2"

print(func())

u = lambda x,y:x+y

print(u(3,2))


#クラス
class MyClass:
    def __init__(self): #コンストラクタ
        self.name = "myClass!"
    def __del__(self): #デストラクタ
        self.name = ""
    def __str__(self):
        return "MyCass" + self.name
    def getName(self): #getNameメソッド
        return self.name
    def setName(self,name):
        self.name = name

a = MyClass()
a.setName("poi")
print(a.getName())
print(a)

#継承
class MyClass2(MyClass):
    def world(self):
        print("hello")

b = MyClass2()
b.setName("hoge")
b.world()
