import csv
import random

def eat_dinner(foods,stomach):
    sum_tastiness = 0
    cur_stomach = stomach
    #your code goes here.
    return sum_tastiness

def test_eat_dinner():
    #import csv file
    f = open('prob2_input.csv' ,'r')
    rd = csv.reader(f)
    f2= open('prob2_sol.csv' ,'r')
    rd2 = csv.reader(f2)
    
    #test your code
    num_food = -1
    num_case = -1
    size_stomach = -1
    food_type = []
    your_answer = []
    for line in rd:    
        if(num_food == -1):
            num_food = int(line[0])
            num_case = num_food
        elif(num_case > 0):
            food_type.append([int(line[0]),int(line[1]),int(line[2])])
            num_case -= 1
        elif(size_stomach == -1):
            size_stomach = int(line[0])
            a = eat_dinner(food_type,size_stomach)
            print("your answer is %d"%(a))
            your_answer.append(a)
            num_food = -1
            num_case = -1
            size_stomach = -1
            food_type = []
    
    #compare with solution
    idx = 0
    for line in rd2:
        if (your_answer[idx] == int(line[0])):
            print("test %d successed"%(idx+1))
        else:
            print("test %d failed. check your output"%(idx+1))
        idx += 1
    