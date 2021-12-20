import split

file = open("Day7/input.txt", "r")
input = file.readlines()
splitinput = split.split(input[0],',')

xlocs = []
max = int(splitinput[0])
min = int(splitinput[0])
for x in splitinput:
    xlocs.append(int(x))
    if int(x) > max:
        max = int(x)
    if int(x) < min:
        min = int(x)

fuelcosts = []

for y in range(min,max):
    sum = 0
    for x in xlocs:
        sum += abs(x - y)
    fuelcosts.append(sum)

fuelmin = fuelcosts[0]
for z in fuelcosts:
    if z < fuelmin:
        fuelmin = z

print("Minimum fuel cost: " + str(fuelmin))