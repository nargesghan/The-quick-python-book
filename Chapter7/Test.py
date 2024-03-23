# x=[]
# y={}
# y[0]=1


dict_example = {"apple": 1, "banana": 2, "cherry": 3}

keys_view = dict_example.keys()
values_view = dict_example.values()
items_view = dict_example.items()

print(keys_view)  # Output: dict_keys(['apple', 'banana', 'cherry'])
print(values_view)  # Output: dict_values([1, 2, 3])
print(items_view)  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])
