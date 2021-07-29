fileInput = open("./DayFive/input.txt", "r")
rawStringInput = fileInput.read()
inputList = rawStringInput.split("\n")

testData = []

for line in range(0,5):
    testData.append(inputList[line])

print(inputList)

def findSeatId(input):
    upperRow = 127
    lowerRow = 0
    returnRow = 0
    column = [0,7]
    for index in range(0,6):
        if input[index] == "F":

