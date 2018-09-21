from math import *
x = int(input())
y = int(input())

res = round(degrees(asin(x/hypot(x,y))))

print("{:d}°".format(res))
