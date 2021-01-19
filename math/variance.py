#!/usr/bin/env python

# 分散の求め方　データの散らばりの度合いを表す値
# 参考　https://sci-pursuit.com/math/statistics/variance.html

# 平均
def Average(numList):
    return sum(numList) / len(numList)

# 偏差
def Deviation(num, average):
    val = num - average
    return val ** 2

# 分散
def Variance(numList):
    average = Average(numList)
    deviationList = []
    for num in numList:
        deviation = Deviation(num, average)
        deviationList.append(deviation)
        
    return sum(deviationList) / len(numList)

def main():
    numList = [71, 80, 89]
    print(Variance(numList))

if __name__ == "__main__":
    main()
