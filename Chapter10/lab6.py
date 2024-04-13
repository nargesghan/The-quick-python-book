def cleanWords(word):
    word=word.strip('!.,:;-? \n-')
    word=word.replace('--','')
    return word

def func(filename,outputfile):
    list=[]
    currentLine=''
    with open(filename) as infile, open(outputfile, "w") as outfile:
        for line in infile:
            # make all one case
            currentLine=line.lower()
            # split into words
            list=currentLine.split()
            for cleaned_words in list:
                cleaned_words=cleanWords(cleaned_words)
                outfile.write(cleaned_words)
                outfile.write('\n')

