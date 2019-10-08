# coding: utf-8
# 論理回路 2.2.1 XORゲート
# パーセプトロンの動作原理式
# {0 (w1x1 +w2x2 ≦ θ) *限界値を閾値θと呼ぶ 
# {1 (w1x1 +w2x2 > θ)
# *重みとバイアスによる方式
# w1 や w2 は入力信号への重 要度をコントロールするパラメータ
# bはニューロンの発火のしやすさ
# {0 (b+w1x1 +w2x2 ≦ 0) θをb（バイアス）にする
# {1 (b+w1x1 +w2x2 > 0)
# NAND、ORの結果をANDに入力することでXORゲートが実現する
# XORは2層のパーセプトロン
from and_gate import AND
from or_gate import OR
from nand_gate import NAND


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))