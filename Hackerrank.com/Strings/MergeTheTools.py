import textwrap
def merge_the_tools(string, k):
    slen = len(string)
    lis = textwrap.wrap(string, k)
    for i in lis:
        i = list(i)
        temp = []
        for j in i:
            if j not in temp:
                temp.append(j)

        i = ''.join(temp)
        print(i)
