def find_tuple_index(input_tuple, item):
    index = input_tuple.index(item)
    return index


my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
print(find_tuple_index(my_tuple, 'c'))
