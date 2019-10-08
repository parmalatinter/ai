# coding: utf-8
# 論理回路 2.2.1 ORゲート
# パーセプトロンの動作原理式
# {0 (w1x1 +w2x2 ≦ θ) *限界値を閾値θと呼ぶ 
# {1 (w1x1 +w2x2 > θ)
# *重みとバイアスによる方式
# w1 や w2 は入力信号への重 要度をコントロールするパラメータ
# bはニューロンの発火のしやすさ
# {0 (b+w1x1 +w2x2 ≦ 0) θをb（バイアス）にする
# {1 (b+w1x1 +w2x2 > 0)
# 0.5,0.5,0

import numpy as np


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))