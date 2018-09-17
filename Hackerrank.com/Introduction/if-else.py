#!/bin/python3

N = int(input())

def isOdd(k):
    if k%2==1:
        return True
    else:
        return False

if isOdd(N):
    print("Weird")
else:
    if (N>20):
        print("Not Weird")
    else:
        if N>=6:
            print("Weird")
        else:
            print("Not Weird")
    

