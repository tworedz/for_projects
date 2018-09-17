def count_substring(string, sub_string):
    k = 0
    while string.find(sub_string)!=-1:
        k+=1
        string = string[string.find(sub_string)+1:]

    return k