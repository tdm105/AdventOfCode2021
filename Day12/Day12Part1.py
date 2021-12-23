import split

file = open("Day12/test.txt", "r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

visitcount = {}
passages = []
for x in input:
    splitinput = split.split(x,'-')
    passages.append(splitinput)
    visitcount[splitinput[0]] = 0
    visitcount[splitinput[1]] = 0
    

paths = []
def explore(inlet, outlet, path,visitcount):
    path += outlet
    visitcount[outlet] += 1
    for x in passages:
        if path[len(path)-len(outlet):] != 'end':
            if x[0] == outlet and x[1] != 'start':
                if (x[0].islower() and visitcount[x[0]] == 0) or (x[0].islower() and x[1].isupper()):
                    explore(x[0],x[1],path,visitcount.copy())
                elif x[1] == 'end':
                    explore(x[0],x[1],path,visitcount.copy())
                if x[0].isupper():
                    if (x[1].islower() and visitcount[x[1]] == 0):
                        explore(x[0],x[1],path,visitcount.copy())
                    elif x[1] == 'end':
                        explore(x[0],x[1],path,visitcount.copy())
            elif x[1] == outlet and x[0] != 'start':
                if x[0].isupper():
                    explore(x[1],x[0],path,visitcount.copy())
                if x[1].isupper():
                    if (x[0].islower() and visitcount[x[0]] == 0):
                        explore(x[1],x[0],path,visitcount.copy())
                    elif x[0] == 'end':
                        explore(x[1],x[0],path,visitcount.copy())
    if path[:5] == 'start' and path[len(path)-len(outlet):] =='end':
        paths.append(path)
        return

for x in passages:
    if x[0] == 'start':
        explore(x[0],x[1],'start',visitcount)
    if x[1] == 'start':
        explore(x[1],x[0],'start',visitcount)

print("Pathcount: " + str(len(set(paths))))