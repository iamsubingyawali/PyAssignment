input_list = [{}, {}, {}, {}]
empty = False

for dicts in input_list:
    if len(dicts) != 0:
        empty = False
        break
    else:
        empty = True

print(empty)
