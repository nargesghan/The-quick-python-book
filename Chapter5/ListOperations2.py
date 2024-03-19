def remove(List , x):
    if x in List:
        del(List[List.index(x)])

#Modify that code to remove the element only if the item occurs in the list more than once
def remove2(List , x):
    if List.count(x)>=2:
        del(List[List.index(x)])


#test remove
List=['Narges','Fara',"Narges","33",12]
remove(List,12)
print(List)

#test remove2
List=['Narges','Fara',"Narges","33",12]
remove2(List,"Fara")
print(List)
remove2(List,"Narges")
print(List)
