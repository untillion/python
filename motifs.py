def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    CountMotifs = Count(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for x in CountMotifs:
            for y in (CountMotifs[symbol]):
                z = y/float(t)
                profile[symbol].append(z)
        
    return profile

def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
    
