def readfile(filepath):
    counts={}
    with open(filepath) as infile:
        for word in infile:
            counts[word]=counts.setdefault(word.strip(),0)+1
    return counts


def mostcountFounder(counts,mostCount,leastCount):
    for word in counts:
        if counts[word]>=mostCount:
            mostCount=counts[word]
        if counts[word]<=leastCount:
            leastCount=counts[word]
    return mostCount,leastCount

def leastFounder(counts,mostCount,leastCount):
    for word in counts:
        if counts[word]==mostCount:
            most.append(word)
        if counts[word]==leastCount:
            least.append(word)
    return least

#lab7

def lab7(filename):
    counts={}
    most=[]
    mostCount=0
    least=[]
    leastCount=1
    counts=readfile(filename)
    mostCount,leastCount=mostcountFounder(counts,mostCount,leastCount)
    least=leastFounder(counts,mostCount,leastCount)
    print(mostCount)
    print(leastCount)
    print(f'most common words: {most}')
    print(f'least common words: {least}')

    








