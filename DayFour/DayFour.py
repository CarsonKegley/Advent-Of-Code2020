f = open(".\DayFour\DayFourData.txt", "r")
content = f.read()
content_list = content.split("\n\n")
searchVariables = ["ecl:","pid:","eyr:","hcl:","byr:","iyr:","hgt:"]
validPassports = 0
#Part One solution
# for index in content_list:
#     if searchVariables[0] in index and searchVariables[1] in index and searchVariables[2] in index and searchVariables[3] in index and searchVariables[4] in index and searchVariables[5] in index and searchVariables[6] in index: 
#         validPassports = 1+ validPassports
print(validPassports)