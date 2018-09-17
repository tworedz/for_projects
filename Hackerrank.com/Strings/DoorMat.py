s = input().split()
n,m = [int(i) for i in s]

pat1 = '.|.'
pat2 = '-'

for i in range(1, n, 2):
    print((pat1*i).center(m, pat2))

print("WELCOME".center(m, pat2))

for i in range(n-2, 0, -2):
    print((pat1*i).center(m, pat2))
