# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 回帰問題は恒等関数
def identity_function(x):
    return x

# 分類問題はソフトマックス関数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    # ニューロン a 隠れ層での重み付き和（重み付き信号とバイアスの総和）
    a1 = np.dot(x, W1) + b1 #行列の積
    # 活性化関数で変換された信号 z
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y




network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # 回帰問題は恒等関数 [ 0.31682708 0.69627909]
print(softmax(y)) # 分類問題はソフトマックス関数 [0.40625907 0.59374093]