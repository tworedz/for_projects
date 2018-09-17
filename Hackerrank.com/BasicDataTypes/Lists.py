if __name__ == '__main__':
    N = int(input())
    lis  = []
    for i in range(N):
        name, *line = input().split()
        line = [int(i) for i in line]

        if name == "insert":
            lis.insert(line[0], line[1])
        elif name == "print":
            print(lis)
        elif name == "remove":
            lis.remove(line[0])
        elif name == "append":
            lis.append(line[0])
        elif name == "sort":
            lis.sort()
        elif name == "pop":
            lis.pop()
        elif name == "reverse":
            lis.reverse()
        else:
            pass
