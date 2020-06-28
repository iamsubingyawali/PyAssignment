input_list = ['abc', 'xyz', 'aba', '1221', 'cc', 'a', '100']
count = 0

for item in input_list:
    if len(item) > 1:
        if item[0] == item[-1]:
            count += 1

print(count)
