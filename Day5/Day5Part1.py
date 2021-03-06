import split

class Coords:
    def __init__(self,extx,exty) -> None:
        self.x = extx
        self.y = exty

class Pair:
    def __init__(self,begin,end) -> None:
        self.begin = begin
        self.end = end
file = open("Day5/input.txt", "r")
input = file.readlines()
for x in range(len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

pairs = []
for x in input:
    pairs.append(split.split(x, ' -> '))

newpairs = []
maxx = 0
maxy = 0
for i in pairs:
    for j in i:
        temp = split.split(j,',')
        x = int(temp[0])
        y = int(temp[1])
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        newpairs.append(Coords(x,y))

finalpairs = []
for k in range(1,len(newpairs),2):
        if newpairs[k-1].x == newpairs[k].x:
            if newpairs[k-1].y > newpairs[k].y:
                finalpairs.append(Pair(newpairs[k],newpairs[k-1]))
            else:
                finalpairs.append(Pair(newpairs[k-1],newpairs[k]))
        if newpairs[k-1].y == newpairs[k].y:
            if newpairs[k-1].x > newpairs[k].x:
                finalpairs.append(Pair(newpairs[k],newpairs[k-1]))
            else:
                finalpairs.append(Pair(newpairs[k-1],newpairs[k]))

board = []
boardy = []
for a in range(maxx+1):
    for b in range(maxy+1):
        boardy.append(0)
    board.append(boardy.copy())
    boardy.clear()

for l in finalpairs:
    if l.begin.x == l.end.x:
        for c in range(l.begin.y,l.end.y+1):
            board[l.begin.x][c] += 1
    if l.begin.y == l.end.y:
        for c in range(l.begin.x,l.end.x+1):
            board[c][l.begin.y] += 1

overlap = 0
for x in board:
    for y in x:
        if y >= 2:
            overlap += 1

print("Overlap: " + str(overlap))