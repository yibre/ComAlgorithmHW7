# -*- coding: utf-8 -*-
import csv
import random


def minnum(arr, target):
    # initialize
    D = [0 for i in range(target + 1)]
    # your code goes in here

    for i in range(1, target + 1):
        D[i] = 9999 # 목표 액수보다 더 큰 금액으로 설정

    coin = [0]
    for i in range(0, len(arr)):
        coin.append(arr[i])

    for i in range(1, len(coin)):
        if coin[i] <= target:
            for j in range(coin[i], target+1):
                D[j] = min(D[j], D[j-coin[i]]+1)
            print(D)
    # return
    if (D[target] == -1) or (D[target] == 9999):
        return -1
    else:
        return D[target]

def test_minnum():
    # import csv
    f = open('prob1_input.csv', 'r')
    rd = csv.reader(f)
    f2 = open('prob1_sol.csv', 'r')
    rd2 = csv.reader(f2)

    # test your code
    temp_result = []
    for line in rd:
        arr = []
        target = 0
        int_number = int(line[0])
        for i in range(int_number):
            arr.append(int(line[i + 1]))
        target = int(line[-1])
        res = minnum(arr, target)
        temp_result.append(res)

    # compare with solution
    idx = 0
    for line in rd2:
        if (temp_result[idx] == int(line[0])):
            print("test %d success." % (idx + 1))
        else:
            print("test %d failed." % (idx + 1))
        idx += 1