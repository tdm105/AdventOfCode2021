import split

file = open("Day8/input.txt", "r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]\

splitinput = []
inputstuff = []
output = []
for x in input:
    splitinput.append(split.split(x, ' | '))

for x in splitinput:
    inputstuff.append(split.split(x[0], ' '))
    output.append(split.split(x[1], ' '))

ones = 0
fours = 0
sevens = 0
eights = 0

for y in output:
    for z in y:
        if len(z) == 2:
            ones += 1
        if len(z) == 4:
            fours += 1
        if len(z) == 3:
            sevens += 1
        if len(z) == 7:
            eights += 1

total = ones + fours + sevens + eights

print("Total: " + str(total))