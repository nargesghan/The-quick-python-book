'''
In the previous lab, you took the text of the first chapter of Moby Dick, normalized the
case, removed punctuation, and wrote the separated words to a file. In this lab, you
read that file, use a dictionary to count the number of times each word occurs, and then
report the most common and least common words.
'''
counts={}
with open("D:\CS internship\step 2\Chapter6\moby_01_clean.txt") as infile:
    for word in infile:
        counts[word]=counts.setdefault(word.strip(),0)+1

most=[]
mostCount=0
least=[]
leastCount=1

for word in counts:
    if counts[word]>=mostCount:
        mostCount=counts[word]
    if counts[word]<=leastCount:
        leastCount=counts[word]

for word in counts:
    if counts[word]==mostCount:
        most.append(word)
    if counts[word]==leastCount:
        least.append(word)

print(mostCount)
print(leastCount)
print(f'most common words: {most}')
print(f'least common words: {least}')


