#!/usr/bin/env python

# グラフの表示
# 参考　https://techacademy.jp/magazine/34230

import sympy as sym
from sympy.plotting import plot

# グラフ
def Graph(y, xRange):
    plot(y, xRange)

def main():
    # 変数として使用する文字を指定する
    x, y = sym.symbols("x y")
    # y = x^2 + 2x - 3
    y = x ** 2 + 2 * x - 3
 
    # 微分
    y = sym.Derivative(y).doit()
    print(y)
    Graph(y, (x, -10, 10))


if __name__ == "__main__":
    main()
