import re

if __name__ == '__main__':
    
    s = input()
    
    if (re.search(r"[a-zA-Z0-9]", s)):
        print(True)
    else: 
        print(False)
    
    if (re.search(r"[a-zA-Z]", s)):
        print(True)
    else: 
        print(False)
    
    if (re.search(r"[0-9]", s)):
        print(True)
    else: 
        print(False)
    
    if (re.search(r"[a-z]", s)):
        print(True)
    else: 
        print(False)
    
    if (re.search(r"[A-Z]", s)):
        print(True)
    else: 
        print(False)

