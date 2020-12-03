from operator import xor
f = open(".\DayTwo\DayTwoData.txt", "r")
content = f.read()
content_list = content.split("\n")
cleanedInputs = []
upperAndLowerBounds = []
searchLetter = []
searchString = []
validPasswords = 0

for line in content_list:
    cleanedInputs.append(line.split())

for index in range(0, len(cleanedInputs)):
    upperAndLowerBounds.append(cleanedInputs[index][0].split("-"))
    searchLetter.append(cleanedInputs[index][1][0])
    searchString.append(cleanedInputs[index][2])

#Solution one commented out to save space and time
# for index in range(0, len(cleanedInputs)):
#     temp = searchString[index].count(searchLetter[index])
#     if temp <= int(upperAndLowerBounds[index][1]) and temp >= int(upperAndLowerBounds[index][0]):
#         validPasswords = 1 + validPasswords

for index in range(0, len(cleanedInputs)):
    letter = searchLetter[index]
    upper = int(upperAndLowerBounds[index][1])-1
    lower = int(upperAndLowerBounds[index][0])-1
    if upper <= len(searchString[index]) -1 :
        if xor(bool(searchString[index][upper] == letter), bool(searchString[index][lower] == letter)):
            validPasswords = validPasswords + 1

print(validPasswords)