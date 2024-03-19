x=[[1, 2, 3], [2,1, 3], [4, 0, 1]] 
#sort this list by the second element in each list
def return_second_element(list):
    return list[1]

z=sorted(x,key=return_second_element)
print(z)
