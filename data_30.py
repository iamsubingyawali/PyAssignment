def check_duplicate(dict_input, check_key):
    status = False
    for keys in dict_input.keys():
        if str(keys) == str(check_key):
            status = True
            break
        else:
            status = False
    return status


input_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(check_duplicate(input_dict, 8))
