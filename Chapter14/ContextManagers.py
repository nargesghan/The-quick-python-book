'''Assume that you’re using a context manager in a script that reads and/or writes several
files. Which of the following approaches do you think would be best?
Put the entire script in a block managed by a with statement.
Use one with statement for all file reads and another for all file writes.
Use a with statement each time you read a file or write a file (for each line, for
example).
Use a with statement for each file that you read or write.
'''

#Use a with statement for each file that you read or write:


'''This is the best practice. It ensures that each file is properly managed, opened, and closed when its block is executed.
 It also keeps the code clean, readable, and ensures resources are properly released after file operations.'''

