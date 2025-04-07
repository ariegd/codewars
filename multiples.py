#!/usr/bin/python3

def solution(number):
    sum=0
    for x in range(1, number):
        print("x = ", x)
        if not(x%3) or not(x%5):
            print("x%3 = ", x%3)
            print("x%5 = ",x%5)
            sum += x   
    return sum
    
print("La suma: ", solution(6))
