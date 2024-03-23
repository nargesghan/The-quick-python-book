# The keys of the dictionary can be tuples representing the cell coordinates (row, column), and the values can be the contents of the cells
# Initialize an empty dictionary to represent the spreadsheet
spreadsheet = {}

# Store a value in cell (2, 3)
spreadsheet[(2, 3)] = 'Hello, World!'

# Retrieve the value in cell (2, 3)
print(spreadsheet[(2, 3)])  # Output: 'Hello, World!'
