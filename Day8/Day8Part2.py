import split

def parse(z, nums, possiblea, possibleb, possiblec, possibled, possiblee, possiblef, possibleg, reparse):
    if len(z) == 2:
        nums[1] = set(z)
        if len(possiblec) == 0:
            possiblec = set(z)
        else:
            possiblec &= set(z)
        if len(possiblef) == 0:
            possiblef = set(z)
        else:
            possiblef &= set(z)
    elif len(z) == 4:
        nums[4] = set(z)
        if len(possiblec) == 0:
            possiblec = set(z)
        else:
            possiblec &= set(z)
        if len(possibleb) == 0:
            possibleb = set(z)
        else:
            possibleb &= set(z)
        if len(possibled) == 0:
            possibled = set(z)
        else:
            possibled &= set(z)
        if len(possiblef) == 0:
            possiblef = set(z)
        else:
            possiblef &= set(z)
    elif len(z) == 3:
        nums[7] = set(z)
        if len(possiblea) == 0:
            possiblea = set(z)
        else:
            possiblea &= set(z)
        if len(possiblec) == 0:
            possiblec = set(z)
        else:
            possiblec &= set(z)
        if len(possiblef) == 0:
            possiblef = set(z)
        else:
            possiblef &= set(z)
    elif len(z) == 5:
        if len(nums[7] & set(z)) == 3:
            nums[3] = set(z)
            if len(possiblea) == 0:
                possiblea = set(z)
            else:
                possiblea &= set(z)
            if len(possiblec) == 0:
                possiblec = set(z)
            else:
                possiblec &= set(z)
            if len(possiblef) == 0:
                possiblef = set(z)
            else:
                possiblef &= set(z)
            if len(possibled) == 0:
                possibled = set(z)
            else:
                possibled &= set(z)
            if len(possibleg) == 0:
                possibleg = set(z)
            else:
                possibleg &= set(z)
        elif len(nums[7] & set(z)) == 2:
            if len(nums[4] & set(z)) == 2:
                nums[2] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possiblec) == 0:
                    possiblec = set(z)
                else:
                    possiblec &= set(z)
                if len(possiblee) == 0:
                    possiblee = set(z)
                else:
                    possiblee &= set(z)
                if len(possibled) == 0:
                    possibled = set(z)
                else:
                    possibled &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
            elif len(nums[4] & set(z)) == 3:
                nums[5] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possibleb) == 0:
                    possibleb = set(z)
                else:
                    possibleb &= set(z)
                if len(possiblef) == 0:
                    possiblef = set(z)
                else:
                    possiblef &= set(z)
                if len(possibled) == 0:
                    possibled = set(z)
                else:
                    possibled &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
            else:
                reparse.append(z)
        elif len(nums[4] & set(z)) == 3:
            if len(nums[1] & set(z)) == 2:
                nums[3] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possiblec) == 0:
                    possiblec = set(z)
                else:
                    possiblec &= set(z)
                if len(possiblef) == 0:
                    possiblef = set(z)
                else:
                    possiblef &= set(z)
                if len(possibled) == 0:
                    possibled = set(z)
                else:
                    possibled &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
            elif len(nums[1] & set(z)) == 1:
                nums[5] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possibleb) == 0:
                    possibleb = set(z)
                else:
                    possibleb &= set(z)
                if len(possiblef) == 0:
                    possiblef = set(z)
                else:
                    possiblef &= set(z)
                if len(possibled) == 0:
                    possibled = set(z)
                else:
                    possibled &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
            else:
                reparse.append(z)
        elif len(nums[4] & set(z)) == 2:
            nums[2] = set(z)
            if len(possiblea) == 0:
                possiblea = set(z)
            else:
                possiblea &= set(z)
            if len(possiblec) == 0:
                possiblec = set(z)
            else:
                possiblec &= set(z)
            if len(possiblee) == 0:
                possiblee = set(z)
            else:
                possiblee &= set(z)
            if len(possibled) == 0:
                possibled = set(z)
            else:
                possibled &= set(z)
            if len(possibleg) == 0:
                possibleg = set(z)
            else:
                possibleg &= set(z)
        else:
            reparse.append(z)
    elif len(z) == 6:
        if len(nums[4] & set(z)) == 4:
            nums[9] = set(z)
            if len(possiblea) == 0:
                possiblea = set(z)
            else:
                possiblea &= set(z)
            if len(possibleb) == 0:
                possibleb = set(z)
            else:
                possibleb &= set(z)
            if len(possiblef) == 0:
                possiblef = set(z)
            else:
                possiblef &= set(z)
            if len(possibled) == 0:
                possibled = set(z)
            else:
                possibled &= set(z)
            if len(possibleg) == 0:
                possibleg = set(z)
            else:
                possibleg &= set(z)
            if len(possiblec) == 0:
                possiblec = set(z)
            else:
                possiblec &= set(z)
        elif len(nums[4] & set(z)) == 3:
            if len(nums[1] & set(z)) == 1:
                nums[6] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possibleb) == 0:
                    possibleb = set(z)
                else:
                    possibleb &= set(z)
                if len(possiblef) == 0:
                    possiblef = set(z)
                else:
                    possiblef &= set(z)
                if len(possibled) == 0:
                    possibled = set(z)
                else:
                    possibled &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
                if len(possiblee) == 0:
                    possiblee = set(z)
                else:
                    possiblee &= set(z)
            elif len(nums[1] & set(z)) == 2:
                nums[0] = set(z)
                if len(possiblea) == 0:
                    possiblea = set(z)
                else:
                    possiblea &= set(z)
                if len(possibleb) == 0:
                    possibleb = set(z)
                else:
                    possibleb &= set(z)
                if len(possiblef) == 0:
                    possiblef = set(z)
                else:
                    possiblef &= set(z)
                if len(possiblee) == 0:
                    possiblee = set(z)
                else:
                    possiblee &= set(z)
                if len(possibleg) == 0:
                    possibleg = set(z)
                else:
                    possibleg &= set(z)
                if len(possiblec) == 0:
                    possiblec = set(z)
                else:
                    possiblec &= set(z)
            else:
                reparse.append(z)
        else:
            reparse.append(z)
    elif len(z) == 7:
        nums[8] = set(z)
        if len(possiblea & nums[8]) == 0:
            possiblea = nums[8]
        if len(possibleb & nums[8]) == 0:
            possibleb = nums[8]
        if len(possiblec & nums[8]) == 0:
            possiblec = nums[8]
        if len(possibled & nums[8]) == 0:
            possibled = nums[8]
        if len(possiblee & nums[8]) == 0:
            possiblee = nums[8]
        if len(possiblef & nums[8]) == 0:
            possiblef = nums[8]
        if len(possibleg & nums[8]) == 0:
            possibleg = nums[8]

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

sevensegs = []
possiblea = set()
possibleb = set()
possiblec = set()
possibled = set()
possiblee = set()
possiblef = set()
possibleg = set()

for y in range(0,len(inputstuff)):
    sevensegs.append(['','','','','','',''])
    nums = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
    possiblea = set('abcdefg')
    possibleb = set('abcdefg')
    possiblec = set('abcdefg')
    possibled = set('abcdefg')
    possiblee = set('abcdefg')
    possiblef = set('abcdefg')
    possibleg = set('abcdefg')
    reparse = []
    for z in inputstuff[y]:
        parse(z,nums,possiblea,possibleb,possiblec,possibled,possiblee,possiblef,possibleg,reparse)
    while len(reparse) != 0:
        parse(reparse.pop(),nums,possiblea,possibleb,possiblec,possibled,possiblee,possiblef,possibleg,reparse)
        
            
    for i in range(0,5):
        if len(possiblea) == 1:
            possiblef = possiblef.difference(possiblea)
            possibleb = possibleb.difference(possiblea)
            possiblec = possiblec.difference(possiblea)
            possibled = possibled.difference(possiblea)
            possiblee = possiblee.difference(possiblea)
            possibleg = possibleg.difference(possiblea)
        if len(possibleb) == 1:
            possiblef = possiblef.difference(possibleb)
            possiblea = possiblea.difference(possibleb)
            possiblec = possiblec.difference(possibleb)
            possibled = possibled.difference(possibleb)
            possiblee = possiblee.difference(possibleb)
            possibleg = possibleg.difference(possibleb)
        if len(possiblec) == 1:
            possiblef = possiblef.difference(possiblec)
            possibleb = possibleb.difference(possiblec)
            possiblea = possiblea.difference(possiblec)
            possibled = possibled.difference(possiblec)
            possiblee = possiblee.difference(possiblec)
            possibleg = possibleg.difference(possiblec)
        if len(possibled) == 1:
            possiblef = possiblef.difference(possibled)
            possibleb = possibleb.difference(possibled)
            possiblea = possiblea.difference(possibled)
            possiblec = possiblec.difference(possibled)
            possiblee = possiblee.difference(possibled)
            possibleg = possibleg.difference(possibled)
        if len(possiblee) == 1:
            possiblef = possiblef.difference(possiblee)
            possibleb = possibleb.difference(possiblee)
            possiblea = possiblea.difference(possiblee)
            possiblec = possiblec.difference(possiblee)
            possibled = possibled.difference(possiblee)
            possibleg = possibleg.difference(possiblee)
        if len(possiblef) == 1:
            possiblea = possiblea.difference(possiblef)
            possibleb = possibleb.difference(possiblef)
            possiblec = possiblec.difference(possiblef)
            possibled = possibled.difference(possiblef)
            possiblee = possiblee.difference(possiblef)
            possibleg = possibleg.difference(possiblef)
        if len(possibleg) == 1:
            possiblef = possiblef.difference(possibleg)
            possibleb = possibleb.difference(possibleg)
            possiblea = possiblea.difference(possibleg)
            possiblec = possiblec.difference(possibleg)
            possiblee = possiblee.difference(possibleg)
            possibled = possibled.difference(possibleg)
    sevensegs[y][0] = possiblea.pop()
    sevensegs[y][1] = possibleb.pop()
    sevensegs[y][2] = possiblec.pop()
    sevensegs[y][3] = possibled.pop()
    sevensegs[y][4] = possiblee.pop()
    sevensegs[y][5] = possiblef.pop()
    sevensegs[y][6] = possibleg.pop()

sum = 0
for y in range(0,len(output)):
    zero = set(sevensegs[y][0] + sevensegs[y][1] + sevensegs[y][2] + sevensegs[y][4] + sevensegs[y][5] + sevensegs[y][6])
    one = set(sevensegs[y][2] + sevensegs[y][5])
    two = set(sevensegs[y][0] + sevensegs[y][2] + sevensegs[y][3] + sevensegs[y][4] + sevensegs[y][6])
    three = set(sevensegs[y][0] + sevensegs[y][2] + sevensegs[y][3] + sevensegs[y][5] + sevensegs[y][6])
    four = set(sevensegs[y][1] + sevensegs[y][2] + sevensegs[y][3] + sevensegs[y][5])
    five = set(sevensegs[y][0] + sevensegs[y][1] + sevensegs[y][3] + sevensegs[y][5] + sevensegs[y][6])
    six = set(sevensegs[y][0] + sevensegs[y][1] + sevensegs[y][3] + sevensegs[y][4] + sevensegs[y][5] + sevensegs[y][6])
    seven = set(sevensegs[y][0] + sevensegs[y][2] + sevensegs[y][5])
    eight = set(sevensegs[y][0] + sevensegs[y][1] + sevensegs[y][2] + sevensegs[y][3] + sevensegs[y][4] + sevensegs[y][5] + sevensegs[y][6])
    nine = set(sevensegs[y][0] + sevensegs[y][1] + sevensegs[y][2] + sevensegs[y][3] + sevensegs[y][5] + sevensegs[y][6])
    num = 0

    for z in output[y]:
        if set(z) == zero:
            num += 0
            num *= 10
        elif set(z) == one:
            num += 1
            num *= 10
        elif set(z) == two:
            num += 2
            num *= 10
        elif set(z) == three:
            num += 3
            num *= 10
        elif set(z) == four:
            num += 4
            num *= 10
        elif set(z) == five:
            num += 5
            num *= 10
        elif set(z) == six:
            num += 6
            num *= 10
        elif set(z) == seven:
            num += 7
            num *= 10
        elif set(z) == eight:
            num += 8
            num *= 10
        elif set(z) == nine:
            num += 9
            num *= 10
    num /= 10
    sum += num

print("Sum: " + str(sum))