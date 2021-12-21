import split

def exploreneighbors(val, origin, map, horizontal, vertical):
    for a in origin:
        if a == [vertical,horizontal]:
            return []
    origin.append([vertical,horizontal])
    val.append(map[vertical][horizontal])
    if vertical == 0:
        if horizontal == 0:
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
        elif horizontal == len(map[vertical])-1:
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
        else: 
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
    elif vertical == len(map)-1:
        if horizontal == 0:
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
        elif horizontal == len(map[vertical])-1:
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
        else: 
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
    else:
        if horizontal == 0:
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
        elif horizontal == len(map[vertical])-1:
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
        else: 
            if map[vertical+1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical+1)
            if map[vertical][horizontal-1] != '9':
                exploreneighbors(val,origin,map,horizontal-1,vertical)
            if map[vertical][horizontal+1] != '9':
                exploreneighbors(val,origin,map,horizontal+1,vertical)
            if map[vertical-1][horizontal] != '9':
                exploreneighbors(val,origin,map,horizontal,vertical-1)
    return val

file = open("Day9/input.txt","r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

lowpoints = []
vertloc = []
horizloc = []
for y in range(0,len(input)):
    for x in range(0,len(input[y])):
        if y == 0:
            if x == 0:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            elif x == len(input[y])-1:
                if input[y+1][x] > input [y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            else:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
        elif y == len(input)-1:
            if x == 0:
                if input[y-1][x] > input[y][x] and input[y][x+1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            elif x == len(input[y])-1:
                if input[y-1][x] > input [y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            else:
                if input[y-1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
        else:
            if x == 0:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            elif x == len(input[y])-1:
                if input[y+1][x] > input [y][x] and input[y][x-1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)
            else:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])
                    vertloc.append(y)
                    horizloc.append(x)

val = []
for z in range(0,len(lowpoints)):
    temp = exploreneighbors([],[],input,horizloc[z],vertloc[z])
    val.append(temp)

maxthree = []
maxthreemin = 0
for x in val:
    for y in range(0,len(maxthree)):
        if len(maxthree) == 3:
            if maxthree[y] < maxthree[maxthreemin]:
                maxthreemin = y
    if len(maxthree) != 3:
        maxthree.append(len(x))
    elif len(x) > maxthree[maxthreemin]:
        maxthree[maxthreemin] = len(x)

total = 1
for y in maxthree:
    total *= y
print(total)
