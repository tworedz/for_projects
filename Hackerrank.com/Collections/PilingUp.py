from collections import Counter, OrderedDict, deque

flags = []

for i in range(int(input())):
    x = int(input())
    n = deque(map(int, input().split()))
    q = []
    for _ in range(len(list(n))):
        if n[0]>n[-1]:
            q.append(n.popleft())
        else:
            q.append(n.pop())
    if q == sorted(q, reverse=True):
        flags.append("Yes")
    else:
        flags.append("No")
        
print('\n'.join(flags))