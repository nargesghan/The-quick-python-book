x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']

def deleteQ(str):
    if str.endswith('"'):
        print(str)
        x[x.index(str)]=str.strip('"')

for str in x:
    deleteQ(str)

print(x)