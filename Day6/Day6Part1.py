import split

file = open("Day6/input.txt","r")
input = file.readlines()
splitinput = split.split(input[0],',')
lanternfish = []
for x in splitinput:
    lanternfish.append(int(x))
total = []

print("Initial: " + str(lanternfish))
for days in range(0,81):
    fishtoadd = []
    total.append(len(lanternfish))
    for fish in range(0,len(lanternfish)):
        if lanternfish[fish] == 0:
            lanternfish[fish] = 6
            fishtoadd.append(8)
        else:
            lanternfish[fish] -= 1
    for add in range(len(fishtoadd)):
        lanternfish.append(fishtoadd.pop())
    print("Day " + str(days+1) + ": " + str(lanternfish))

print("Totals: " + str(total))