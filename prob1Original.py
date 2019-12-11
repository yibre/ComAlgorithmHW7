import csv
import random

def minnum(arr,target):
    #initialize
    D = [0 for i in range(target+1)]
    
    #your code goes in here
    
    #return
    if (D[target] == -1) or (D[target] == 9999):
        return -1
    else:
        return D[target]

def test_minnum():
    #import csv
    f = open('prob1_input.csv' ,'r')
    rd = csv.reader(f)
    f2 = open('prob1_sol.csv' ,'r')
    rd2 = csv.reader(f2)
    
    #test your code
    temp_result = []
    for line in rd:
        arr = []
        target = 0
        int_number = int(line[0])
        for i in range(int_number):
            arr.append(int(line[i+1]))
        target = int(line[-1])
        res = minnum(arr,target)
        temp_result.append(res)
        
    #compare with solution
    idx = 0
    for line in rd2:
        if (temp_result[idx] == int(line[0])):
            print("test %d success."%(idx+1))
        else:
            print("test %d failed."%(idx+1))
        idx += 1
    