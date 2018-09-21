from itertools import groupby
for i, j in groupby(input()):
    print('({}, {})'.format(len(list(j)), i), end=' ')