import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

print("Hello, world!")

a = np.array([0,1,2,3,4,5])
print(a.ndim)
print(a.shape) # 各次元の長さ

b = a.reshape((3,2)) # 2次元配列に変換
print(b)
print(b.shape)


b[1][0] = 77
print(b)
print(a) # aにも変更を受ける、そうならないようにするにはコピーする。

c = np.array([0,1,2,3])
d = c.copy()
e = c.reshape((2,2))
c[2] = 10
print(c)
print(d) # cの変更に影響をうけない
print(e) # cの変更に影響をうけている

a = np.array([0,1,2])
print(a*2)

a = np.array([0,1,2,3,4,5,6])
print(a[np.array([0,1,4])]) # 0,1,4番めを取ってくる
print(a>3) #[F,F,F,F,T,T,T]
print(a[a>3]) # [4,5,6]
a[a>3] = 3 # a>3のものをすべて3にする
print(a)

a = np.array([0,1,2,3,4,5,6])
print(a.clip(2,4)) # 2から4までの数に抑える

# 時間経過ごとのアクセス数からアクセスを予測する。
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10]) # 10個まで表示
print(data.shape) # 各次元の数 (743,2)

# dataを２つにわける
x = data[: ,0]
y = data[: ,1]

print(sp.sum(sp.isnan(y))) # nanのある数を確認

# 予めnanのデータを取り除いておく
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

print(x[:10])
print(y[:10])


# データの散布図を表示
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

# 誤差 fは学習したモデル
def error(f,x,y):
    return sp.sum((f(x) - y) ** 2)

# 多項式フィット
# 第３項目の1 近似する多項式の数 1としたら直線
# full 近似プロセスの情報を返す
# residual 近似誤差
fp1, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)

print("Model parameters: %s" % fp1) # [    2.57152281  1002.10684085]
print("residuals %s" % residuals) # [  3.19874315e+08]

# f(x) = 2.57152281 * x + 1002.10684085

#　モデルパラメータからモデル関数を作る。
f1 = sp.poly1d(fp1)
print(error(f1,x,y))


fx = sp.linspace(0,x[-1],1000) # プロット用にx値を作成
plt.plot(fx,f1(fx), linewidth=4)
plt.legend()



# 次数２の多項式曲線であてはめ
fp2 = sp.polyfit(x,y,2)
print(fp2)
f2 = sp.poly1d(fp2)
print(error(f2,x,y))
plt.plot(fx,f2(fx),linestyle = "--", linewidth=4)

# 次数100の多項式曲線であてはめ
fp100 = sp.polyfit(x,y,100)
print(fp100)
f100 = sp.poly1d(fp100)
print(error(f100,x,y))
plt.plot(fx,f100(fx),linestyle = "-", linewidth=4, color="r")



plt.legend(["d=%i" % f1.order,"d=%i" % f2.order,"d=%i" % f100.order], loc = "upper left")
plt.show()



# データの散布図を表示
plt.scatter(x,y)
plt.title("Web traffic over the last month 2")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

# 急激にかわる3.5週前後で直線２本をつかって近似する

inflection = 3.5*7*24 # 急激に変化する時刻
xa = x[:inflection] # 急激に変化する前の時間
ya = y[:inflection]

xb = x[inflection:] # 急激に変化した後の時間
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa,ya,1))
fb = sp.poly1d(sp.polyfit(xb,yb,1))


fa_error = error(fa,xa,ya)
fb_error = error(fb,xb,yb)

plt.plot(xa,fa(xa),linestyle = "-", linewidth=4)
plt.plot(xb,fb(xb),linestyle = "-", linewidth=4)


print("Error inflection=%f" % (fa_error + fb_error))

# 急激にかわる3.5週前後で2次曲線２本をつかって近似する

f2a = sp.poly1d(sp.polyfit(xa,ya,2))
f2b = sp.poly1d(sp.polyfit(xb,yb,2))

f2a_error = error(f2a,xa,ya)
f2b_error = error(f2b,xb,yb)

plt.plot(xa,f2a(xa),linestyle = "--", linewidth=4)
plt.plot(xb,f2b(xb),linestyle = "--", linewidth=4)

print("Error inflection=%f" % (f2a_error + f2b_error))

# 急激にかわる3.5週前後で100次曲線2本をつかって近似する

f100a = sp.poly1d(sp.polyfit(xa,ya,100))
f100b = sp.poly1d(sp.polyfit(xb,yb,100))

f100a_error = error(f100a,xa,ya)
f100b_error = error(f100b,xb,yb)

plt.plot(xa,f100a(xa),linestyle = "-", linewidth=4, color="r")
plt.plot(xb,f100b(xb),linestyle = "-", linewidth=4, color="r")

print("Error inflection=%f" % (f100a_error + f100b_error))



#plt.show()


# データの散布図を表示



plt.clf()
plt.scatter(x,y, color="b")
plt.title("Web traffic over the last month 3")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

# 急激にかわる3.5週以降のデータを使って学習する

print(xb[:10])
print(yb[:10])
print(x[:10])
print(y[:10])


f1 = sp.poly1d(sp.polyfit(xb,yb,1))
f2 = sp.poly1d(sp.polyfit(xb,yb,2))
f3 = sp.poly1d(sp.polyfit(xb,yb,3))
f4 = sp.poly1d(sp.polyfit(xb,yb,4))
f100 = sp.poly1d(sp.polyfit(xb,yb,100))

f1_error = error(f1,x,y)
f2_error = error(f2,x,y)
f3_error = error(f3,x,y)
f4_error = error(f4,x,y)
f100_error = error(f100,x,y)

plt.plot(x,f1(x),linestyle = "-", linewidth=4)
plt.plot(x,f2(x),linestyle = "-", linewidth=4)
plt.plot(x,f3(x),linestyle = "-", linewidth=4)
plt.plot(x,f4(x),linestyle = "-", linewidth=4)
plt.plot(x,f100(x),linestyle = "-", linewidth=4)


plt.legend(["d=%i" % f1.order,
            "d=%i" % f2.order,
            "d=%i" % f3.order,
            "d=%i" % f4.order,
            "d=%i" % f100.order], loc = "upper left")



plt.show()









