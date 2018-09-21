from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
mas = OrderedCounter(input() for _ in range(int(input())))

print(len(mas))
print(*mas.values(), sep=' ')