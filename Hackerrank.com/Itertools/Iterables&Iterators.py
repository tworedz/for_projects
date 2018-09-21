from itertools import combinations as comb
n = int(input())
mas = input().split()
k = int(input())
mas = list(comb(mas, k))
lis = list(filter(lambda x: ('a' in x), mas))
print(round(len(lis)/len(mas), 4))