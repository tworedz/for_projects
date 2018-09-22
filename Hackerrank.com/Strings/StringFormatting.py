def print_formatted(number):
    # your code goes here
    lenB = len(bin(n))-1
    for i in range(1, n+1):
        s = "{} ".format(i).rjust(lenB)+\
        "{:o} ".format(i).rjust(lenB)+\
        "{:X} ".format(i).rjust(lenB)+\
        "{:b} ".format(i).rjust(lenB)
        print(s)