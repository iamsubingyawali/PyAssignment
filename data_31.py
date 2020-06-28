input_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for item in input_dict:
    print("Key:", item, end=" ")
    print("Value:", input_dict.get(item))
