import string
def print_rangoli(size):
    # your code goes here
    lis = string.ascii_lowercase

    width = size * 4 - 3
    alpha = [i for i in lis if lis.index(i)<size]
    alpha = alpha[:0:-1] + alpha
    rangoli = []
    rangoli.append('-'.join(alpha))
    
    for i in range(size-1):
        alpha.pop(size-1)
        alpha.pop(size-2)
        size-=1
        rangoli.append('-'.join(alpha))
    
    rangoli = rangoli[:0:-1] + rangoli
    
    for i in rangoli:
        print(i.center(width, '-'))
    