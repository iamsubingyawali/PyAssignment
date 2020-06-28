def create_dict(number):
    new_dict = {}
    for i in range(1, int(number) + 1):
        new_dict[i] = i * i
    return new_dict


num = input("Enter a number: ")
print(create_dict(num))
