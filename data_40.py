def add_to_tuple(input_tuple, item):
    input_tuple = input_tuple + (item,)
    return input_tuple


my_tuple = (1, 2, 3, 4)
print(add_to_tuple(my_tuple, 'abc'))
