import split

file = open("Day11/input.txt", "r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

map = []
for y in input:
    temp = []
    for x in y:
        temp.append(int(x))
    map.append(temp)

def flashcheck(map,y,x,flashsum,flashed):
    if map[y][x] > 9 and flashed[y][x] == 0:
        map[y][x] = 0
        flashed[y][x] = 1
        flashsum += 1
        if y == 0:
            if x == 0:
                map[y][x+1] += 1
                map[y+1][x+1] += 1
                map[y+1][x] += 1
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
            elif x == len(map[y])-1:
                map[y][x-1] += 1
                map[y+1][x-1] += 1
                map[y+1][x] += 1
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
            else:
                map[y][x-1] += 1
                map[y+1][x-1] += 1
                map[y+1][x] += 1
                map[y+1][x+1] += 1
                map[y][x+1] += 1 
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
        elif y == len(map)-1:
            if x == 0:
                map[y][x+1] += 1
                map[y-1][x+1] += 1
                map[y-1][x] += 1
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
            elif x == len(map[y])-1:
                map[y][x-1] += 1
                map[y-1][x-1] += 1
                map[y-1][x] += 1
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
            else:
                map[y][x-1] += 1
                map[y-1][x-1] += 1
                map[y-1][x] += 1
                map[y-1][x+1] += 1
                map[y][x+1] += 1 
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
        else:
            if x == 0:
                map[y][x+1] += 1
                map[y-1][x+1] += 1
                map[y-1][x] += 1
                map[y+1][x+1] += 1
                map[y+1][x] += 1
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
            elif x == len(map[y])-1:
                map[y][x-1] += 1
                map[y-1][x-1] += 1
                map[y-1][x] += 1
                map[y+1][x-1] += 1
                map[y+1][x] += 1
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
            else:
                map[y][x-1] += 1
                map[y-1][x-1] += 1
                map[y-1][x] += 1
                map[y-1][x+1] += 1
                map[y][x+1] += 1 
                map[y+1][x-1] += 1
                map[y+1][x] += 1
                map[y+1][x+1] += 1
                flashsum = flashcheck(map,y,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x,flashsum, flashed)
                flashsum = flashcheck(map,y-1,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y,x+1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x-1,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x,flashsum, flashed)
                flashsum = flashcheck(map,y+1,x+1,flashsum, flashed)
    return flashsum

flashed = []
for y in range(0,len(map)):
    temp = []
    for x in range(0,len(map[y])):
        temp.append(0)
    flashed.append(temp)


flashsum = 0
for step in range(0,100):
    for y in range(0,len(map)):
        for x in range(0,len(map[y])):
            map[y][x] += 1
    for y in range(0,len(map)):
        for x in range(0,len(map[y])):
            flashsum = flashcheck(map,y,x,flashsum, flashed)
    for y in range(0,len(map)):
        for x in range(0,len(map[y])):
            if flashed[y][x] == 1:
                map[y][x] = 0
            flashed[y][x] = 0
print("Sum: " + str(flashsum))