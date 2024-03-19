import copy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = copy.deepcopy(x)

y[0][0] = 100
print(x)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(y)  # Output: [[100, 2, 3], [4, 5, 6], [7, 8, 9]]

