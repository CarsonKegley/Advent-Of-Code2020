f = open(".\DayThree\DayThreeData.txt", "r")
content = f.read()
content_list = content.split("\n")
testData = ["............#....#.............",
            "...........##....#......#..#..#",
            "......#.......#......#.........",
            "..#.#....#....#.............##.",
            "..#........####....#...#.......",
            "..##.....#.#.#..#.........#....",
            "...#.#..#..#....#..#..#........",
            "#.......#.........#....##.###.."]

def partOne(input, right):
    numberOfTreesHit = 0
    index = 0
    lines = len(input)
    for x in range(0,lines):
        if input[x][index] == "#":
            numberOfTreesHit = 1 + numberOfTreesHit
        index = (index + right) % 31
    return numberOfTreesHit

def partTwo(input):
    numberOfTreesHit = 0
    index = 0
    lines = len(input)
    for x in range(0,lines, 2):
        if input[x][index] == "#":
            numberOfTreesHit = 1 + numberOfTreesHit
        index = (index + 1) % 31
        
    return numberOfTreesHit

# print(partOne(content_list,3)) 
# print(partOne(content_list,1))
# print(partOne(content_list,5))
# print(partOne(content_list,7))
# print(partTwo(content_list))

returnList = partOne(content_list,3) * partOne(content_list,1) * partOne(content_list,5) * partOne(content_list,7) * partTwo(content_list)
print(returnList)