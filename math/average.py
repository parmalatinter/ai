#!/usr/bin/env python

# 平均の求め方

def Average(numList):
    return sum(numList) / len(numList)
    
def main():
    numList = [1, 2, 3]
    print(Average(numList))

if __name__ == "__main__":
    main()