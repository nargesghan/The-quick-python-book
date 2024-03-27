'''
What list comprehension would you use to process the list x so that all negative values
are removed?
'''
x = [1, 3, 5, 0, -1, 3, -2]

non_negative=[item for item in x if item>=0]
print(non_negative)

'''
Create a generator that returns only odd numbers from 1 to 100. (Hint: A number is
odd if there is a remainder if divided by 2; use % 2 to get the remainder of division by
2.)
'''
odd=(number for number in range(0,100) if number%2!=0)
print(list(odd))


''' Write the code to create a dictionary of the numbers and their cubes from 11 through 15.
'''

cubes={item:item**3 for item in range(11,16)}

print(cubes)


