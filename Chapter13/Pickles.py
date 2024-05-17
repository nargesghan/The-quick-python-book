'''Think about why a pickle would or would not be a good solution in the following use
'''

# cases:

# Saving some state variables from one run to the next

'''Pickling allows you to store the state of an object and restore it later, 
which can be useful for saving game progress, user preferences, or other types of application state.
'''

#Keeping a high­score list for a game

'''allowing you to easily load and update the list as needed.'''


# Storing usernames and passwords

'''Pickled data is not encrypted, so it's not secure to store sensitive information like passwords.
 Instead, you should use a secure method like hashing and salting to store passwords'''

#Storing a large dictionary of English terms

'''if your data is big, database is better choice'''