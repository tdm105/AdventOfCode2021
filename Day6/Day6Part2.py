import split

def fishTick(lanternfish, fishtoadd, fish):
    if lanternfish[fish] == 0:
        lanternfish[fish] = 6
        fishtoadd.append(8)
    else:
        lanternfish[fish] -= 1

file = open("Day6/test.txt","r")
input = file.readlines()
splitinput = split.split(input[0],',')
lanternfish = []
for x in splitinput:
    lanternfish.append(int(x))
total = []

print("Initial: " + str(lanternfish))
for days in range(0,257):
    fishtoadd = []
    total.append(len(lanternfish))
    for fish in range(0,len(lanternfish)):
        fishTick(lanternfish,fishtoadd,fish)
    for add in range(len(fishtoadd)):
        lanternfish.append(fishtoadd.pop())
    #print("Day " + str(days+1) + ": " + str(lanternfish))

print("Totals: " + str(total))