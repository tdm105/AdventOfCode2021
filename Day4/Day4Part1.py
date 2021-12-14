import split
import copy
input = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n22 13 17 11 0\n8 2 23 4 24\n21 9 14 16 7\n6 10 3 18 5\n1 12 20 15 19\n\n3 15 0 2 22\n9 18 13 17 5\n19 8 7 25 23\n20 11 10 24 4\n14 21 16 12 6\n\n14 21 17 24 4\n10 16 15 9 19\n18 8 23 26 20\n22 11 13 6 5\n2 0 12 3 7"

splitinput = split.split(input, '\n\n')

calls = split.split(splitinput[0], ',')

splitinput.pop(0)
boards = splitinput.copy()

bingoboards = []
for x in boards:
    bingoboards.append(split.split(x, '\n'))

bingo = []
temp = []
for x in bingoboards:
    for y in x:
        temp.append(split.split(y, ' '))
    bingo.append(temp.copy())
    temp.clear()

called = copy.deepcopy(bingo)
for board in range(len(called)):
        for row in range(len(called[board])):
            for column in range(len(called[board][row])):
                called[board][row][column] = 0

for x in calls:
    for board in range(len(bingo)):
        for row in range(len(bingo[board])):
            for column in range(len(bingo[board][row])):
                if bingo[board][row][column] == x:
                    called[board][row][column] = 1
                    print(str(row) + "," + str(column))
