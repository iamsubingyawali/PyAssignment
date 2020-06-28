word = input("Enter a word: ")
result = {}
for letter in word:
    if result.get(letter) is None:
        result[letter] = 1
    else:
        result[letter] = result.get(letter) + 1
resultList = list(result.items())

# Implementing bubble sort
for _ in range(0, len(resultList)):
    for j in range(0, len(resultList)-1):
        if resultList[j][1] < resultList[j+1][1]:
            resultList[j], resultList[j+1] = resultList[j+1], resultList[j]

sortedResult = {}

for item in resultList:
    sortedResult[item[0]] = item[1]

print(sortedResult)
