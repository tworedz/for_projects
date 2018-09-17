masName = []
masScore = []

if __name__ == '__main__':
    for _ in range(int(input())):
        masName.append(input())
        masScore.append(float(input()))
    
    m = min(masScore)
    
    while min(masScore) == m:
        masName.remove(masName[masScore.index(m)])
        masScore.remove(masScore[masScore.index(m)])
    

    m = min(masScore)
    mas = []
    for i in range(len(masScore)):
        if masScore[i] == m:
            mas.append(masName[i])
    mas.sort()
    
    for i in mas: print(i)