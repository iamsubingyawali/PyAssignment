string_1 = input("Enter String1: ")
string_2 = input("Enter String2: ")

list_1 = list(string_1)
list_2 = list(string_2)

list_1[0], list_2[0] = list_2[0], list_1[0]
list_1[1], list_2[1] = list_2[1], list_1[1]

string_1 = "".join(list_1)
string_2 = "".join(list_2)

resultString = string_1+' '+string_2
print(resultString)
