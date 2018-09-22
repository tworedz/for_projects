def minion_game(string):
    vowel = 'AEIOU'
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if s[i] in vowel:
            Kevin += len(string)-i
        else: 
            Stuart += len(string)-i
    if Kevin>Stuart:
        print("Kevin {}".format(Kevin))
    elif Stuart>Kevin:
        print("Stuart {}".format(Stuart))
    else:
        print("Draw")