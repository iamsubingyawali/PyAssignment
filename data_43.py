def delete_from_tuple(input_tuple, item_to_remove):
    input_list = list(input_tuple)
    input_list.remove(item_to_remove)
    tuple_out = tuple(input_list)
    return tuple_out


my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
print(delete_from_tuple(my_tuple, 'a'))
print(delete_from_tuple(my_tuple, 'e'))
