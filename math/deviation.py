#!/usr/bin/env python

# 偏差の求め方 母集団の中でどれくらいの位置にいるかを表す数値
# https://shingakunet.com/journal/column/20160228100500/

# 平均
def Average(numList):
    return sum(numList) / len(numList)

# 偏差
def Deviation(num, average):
    val = num - average
    return val ** 2

def main():
    numList = [1, 2, 3]
    average = Average(numList)
    for num in numList:
        print(Deviation( num, average))
   

if __name__ == "__main__":
    main()