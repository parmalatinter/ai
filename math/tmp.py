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
 
    # 8 = x^2 - 12x 
    eq = sym.Eq(x**2-12*x, -8)
    # 方程式を解く
    # [6 - 2*sqrt(7), 2*sqrt(7) + 6]
    print(eq)
    print(sym.solve(eq))

    # 微分
    y = sym.Derivative(y).doit()
    print(y)
    Graph(y, (x, -10, 10))

    # 積分
    y = sym.Integral(y).doit()
    print(y)
    Graph(y, (x, -10, 10))

if __name__ == "__main__":
    main()
