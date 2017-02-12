from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris() # sklearnよりロード

# 閾値を計算して分類する。

features = data['data'] # 特徴量 4種　すでに画像データから抽出されているとする。
# 特徴量の名前 ['sepal length (cm)',　がく片
#'sepal width (cm)',がく片
#'petal length (cm)',花弁
#'petal width (cm)'] 花弁

feature_names = data['feature_names']
target = data['target'] # 花の種類 3種
target_names = data['target_names'] #花の名前 ['setosa' 'versicolor' 'virginica']
labels = target_names[target] # 各 データに対する回答の花の名前

print(features)
print(feature_names)
print(target)
print(target_names)


plt.title("flower")

def show(i,j,n):
    plt.subplot(2, 3, n+1)
    plt.xlabel(feature_names[i])
    plt.ylabel(feature_names[j])
    plt.autoscale(tight=True)
    plt.grid()

    for t,marker,c in zip(range(3), ">ox", "rgb"):
        plt.scatter(features[target == t, i],
                    features[target == t, j],
                    marker = marker,
                    c = c
                    )

show(0,1,0)
show(1,2,1)
show(2,3,2)
show(0,2,3)
show(0,3,4)
show(1,3,5)

# plt.show()

# 花弁の長さでSetosaを他の花と見分けることができるとあたりをつける。
plength = features[:,2] # 花弁の長さの特徴量のみ取り出す
is_setosa = (labels == 'setosa') # setosaかどうかのブーリアン配列を生成

print(is_setosa)

# 最大のもの
max_setosa = plength[is_setosa].max()
# 最小のもの
min_non_setosa = plength[~is_setosa].min()

print("Maximum setosa: {0}.".format(max_setosa)) # 1.9
print("Minimum others: {0}.".format(min_non_setosa)) # 3.0

# よって花弁の長さが2以下ならsetosa

def apply_model(example):
    if example[2] < 2: print('Iris Setosa')
    else: print('Iris Virginica or Iris Versicolor')

for x in features:
    apply_model(x)

## Setosa以外の特徴量とラベルを選ぶ
features = features[~is_setosa] # setosaでないもの
labels = labels[~is_setosa] # setosaでないもの
virginica = ( labels == 'virginica') # virginicaのみ

print(features.shape[1]) # 特徴量 4種
print(range(features.shape[1])) #各特徴量の範囲

best_acc = -1.0
best_fi = -1
best_t = -1.0

for fi in range(features.shape[1]):
#しきい値候補
    thresh = features[:, fi].copy()
    thresh.sort

    for t in thresh:
        pred = (features[:, fi] > t) # 予測結果の列
        acc = (labels[pred] == 'virginica').mean() # 答え合わせ
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t

print(best_acc) # 1.0
print(best_fi) # 0
print(best_t) # 7.0

# 求めたモデルで計算
def apply_model2( example ):
    if example[best_fi] > best_t: print('virginica')
    else: print('versicolor')


for x in features:
    apply_model2(x)






