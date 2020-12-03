f = open(".\DayOne\DayOneData.txt", "r")
content = f.read()
content_list = content.split("\n")
content_list = [int(i) for i in content_list]
list.sort(content_list)

returnVal = 0  

def recurse(findFor):
    for val in content_list:
        valInverse = findFor - val
        if content_list.count(valInverse) != 0:
            return  valInverse * val
            

for val in content_list:
        valInverse = 2020 - val
        temp = recurse(valInverse)
        if type(temp) == int  and temp != 0:
            returnVal = temp * val
            break

print(returnVal)


