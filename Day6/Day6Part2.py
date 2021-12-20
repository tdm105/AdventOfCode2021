import split

file = open("Day6/input.txt","r")
input = file.readlines()
splitinput = split.split(input[0],',')
lanternfish = []
for x in splitinput:
    lanternfish.append(int(x))
total = []

print("Initial: " + str(lanternfish))

fishies = []
for x in range(0,9):
    fishies.append(0)

for fish in lanternfish:
    fishies[fish] += 1

for days in range(0,257):
    temptotal = 0
    fishtoadd = 0
    for fish in fishies:
        temptotal += fish
    total.append(temptotal) 
    if fishies[0] > 0:
        fishtoadd = fishies[0]
        fishies[0] = 0
    for y in range(1,len(fishies)):
        if fishies[y] > 0:
            fishies[y-1] = fishies[y]
            fishies[y] = 0
    
    fishies[6] += fishtoadd
    fishies[8] += fishtoadd

print("Totals: " + str(total))