import split

file = open("Day9/input.txt","r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

lowpoints = []
for y in range(0,len(input)):
    for x in range(0,len(input[y])):
        if y == 0:
            if x == 0:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x]:
                    lowpoints.append(input[y][x])
            elif x == len(input[y])-1:
                if input[y+1][x] > input [y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
            else:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
        elif y == len(input)-1:
            if x == 0:
                if input[y-1][x] > input[y][x] and input[y][x+1] > input[y][x]:
                    lowpoints.append(input[y][x])
            elif x == len(input[y])-1:
                if input[y-1][x] > input [y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
            else:
                if input[y-1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x]:
                    lowpoints.append(input[y][x])
        else:
            if x == 0:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])
            elif x == len(input[y])-1:
                if input[y+1][x] > input [y][x] and input[y][x-1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])
            else:
                if input[y+1][x] > input[y][x] and input[y][x+1] > input[y][x] and input[y][x-1] > input[y][x] and input[y-1][x] > input[y][x]:
                    lowpoints.append(input[y][x])

risklevels = []
risklevelsum = 0
for x in lowpoints:
    risklevels.append(1+int(x))
    risklevelsum += 1+int(x)

print("Risk Level Sum: " + str(risklevelsum))