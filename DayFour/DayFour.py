import re
f = open(".\DayFour\DayFourData.txt", "r")
content = f.read()
content_list = content.split("\n\n")
searchVariables = ["ecl:","pid:","eyr:","hcl:","byr:","iyr:","hgt:"]
validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
numValidPassports = 0

#validPassports = 0
#Part One solution
# for index in content_list:
#     if searchVariables[0] in index and searchVariables[1] in index and searchVariables[2] in index and searchVariables[3] in index and searchVariables[4] in index and searchVariables[5] in index and searchVariables[6] in index: 
#         validPassports = 1+ validPassports


def newLineSanitation(input):
    returnValue = input.replace("\n", " ")
    return returnValue

def validatePassport (input):
    validECL = False
    validPID = False
    validEYR = False
    validHCL = False
    validBYR = False
    validIYR = False
    validHGT = False
    hclRegex = r"^#[a-f0-9]{6}"
    
    for index in range(0,len(input)):
        if input[index][0] == "byr" and int(input[index][1]) >= 1920 and int(input[index][1]) <= 2002:
            validBYR = True
        elif input[index][0] == "iyr" and int(input[index][1]) >= 2010 and int(input[index][1]) <= 2020:
            validIYR = True
        elif input[index][0] == "eyr" and int(input[index][1]) >= 2020 and int(input[index][1]) <= 2030:
            validEYR = True
        elif input[index][0] == "ecl" and validEyeColors.count(input[index][1]) != 0:
            validECL = True
        elif input[index][0] == "pid" and len(input[index][1]) == 9 and int(input[index][1]) > 0:
            validPID = True
        elif input[index][0] == "hcl" and re.match(hclRegex,input[index][1]) != None:
            validHCL = True
        elif input[index][0] == "hgt":
            temp = int(input[index][1].strip("cmin"))
            
            if "cm" in input[index][1] and temp >= 150 and temp <=193:
                validHGT = True
            elif "in" in input[index][1] and temp >= 59 and temp <=76:
                validHGT = True

    return  validHGT and validECL and validPID and validEYR and validHCL and validBYR and validIYR

validPassports = []

for index in content_list:
    if searchVariables[0] in index and searchVariables[1] in index and searchVariables[2] in index and searchVariables[3] in index and searchVariables[4] in index and searchVariables[5] in index and searchVariables[6] in index: 
         validPassports.append(index)


for index in range(0,len(validPassports)):
    validPassports[index] = newLineSanitation(validPassports[index])
    validPassports[index] = validPassports[index].split(" ")
    for i in range(0,len(validPassports[index])):
        validPassports[index][i] = validPassports[index][i].split(":")

for passport in range(0,len(validPassports)):
    if validatePassport(validPassports[passport]):
        numValidPassports = 1+ numValidPassports

# print(validPassports[0])
# print(validatePassport(validPassports[0]))
print(numValidPassports)
