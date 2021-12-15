import split
import copy

file = open("Day4/input.txt", "r")
input = file.readlines()

calls = split.split(input[0], ',')

input.pop(0)
boards = input.copy()

bingoboards = []
firstpos = 0
for x in range(1,len(boards)):
    boards[x] = boards[x].replace('  ', ' ')
    if boards[x][0] == ' ':
        boards[x] = boards[x][1:]
    if boards[x] == '\n':
        lastpos = x
        bingoboards.append(boards[firstpos+1:lastpos])
        firstpos = x
bingoboards.append(boards[firstpos+1:len(boards)])


bingo = []
temp = []
for x in bingoboards:
    for y in x:
        if y[len(y)-1] == '\n':
            y = y[:len(y)-1]
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
                winningboard = called[board][row] == [1,1,1,1,1] or called[board][:][column] == [1,1,1,1,1]
                if winningboard:
                    winner = bingo[board]
                    winnercalls = called[board]
                    winningcall = int(x)
                    break
            if winningboard:
                break
        if winningboard:
            break
    if winningboard:
        break

sum = 0
for row in range(len(winner)):
    for column in range(len(winner[row])):
        if winnercalls[row][column] == 0:
            sum += int(winner[row][column])

score = sum * winningcall

print("Score: " + str(score))




