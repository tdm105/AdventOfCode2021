import split

file = open("Day10/input.txt","r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

errorscore = 0
incompletescores = []

for x in input:
    checkstack = []
    for y in range(1,len(x)):
        incompletescore = 0
        if x[y-1] == '[' or x[y-1] == '<' or x[y-1] == '{' or x[y-1] == '(':
            checkstack.append(x[y-1])
        if y == len(x)-1 and (x[y] == '(' or x[y] == '[' or x[y] == '{' or x[y] == '<'):
            checkstack.append(x[y])
        if len(checkstack) == 0:
            if y == len(x)-1 and len(checkstack) != 0:
                print("Incomplete")
                for z in range(0,len(checkstack)):
                    incompletescore *= 5
                    if checkstack[len(checkstack)-z-1] == '(':
                        incompletescore += 1
                    elif checkstack[len(checkstack)-z-1] == '[':
                        incompletescore += 2
                    elif checkstack[len(checkstack)-z-1] == '{':
                        incompletescore += 3
                    elif checkstack[len(checkstack)-z-1] == '<':
                        incompletescore += 4
                incompletescores.append(incompletescore)
                break
        elif checkstack[len(checkstack)-1] == '[':
            if x[y] == ']':
                checkstack.pop()
            elif x[y] == ')':
                print("Expected ], found )")
                errorscore += 3
                break
            elif x[y] == '}':
                print("Expected ], found }")
                errorscore += 1197
                break
            elif x[y] == '>':
                print("Expected ], found >")
                errorscore += 25137
                break
            if y == len(x)-1 and len(checkstack) != 0:
                print("Incomplete")
                for z in range(0,len(checkstack)):
                    incompletescore *= 5
                    if checkstack[len(checkstack)-z-1] == '(':
                        incompletescore += 1
                    elif checkstack[len(checkstack)-z-1] == '[':
                        incompletescore += 2
                    elif checkstack[len(checkstack)-z-1] == '{':
                        incompletescore += 3
                    elif checkstack[len(checkstack)-z-1] == '<':
                        incompletescore += 4
                incompletescores.append(incompletescore)
                break
        elif checkstack[len(checkstack)-1] == '(':
            if x[y] == ')':
                checkstack.pop()
            elif x[y] == ']':
                print("Expected ), found ]")
                errorscore += 57
                break
            elif x[y] == '}':
                print("Expected ), found }")
                errorscore += 1197
                break
            elif x[y] == '>':
                print("Expected ), found >")
                errorscore += 25137
                break
            if y == len(x)-1 and len(checkstack) != 0:
                print("Incomplete")
                for z in range(0,len(checkstack)):
                    incompletescore *= 5
                    if checkstack[len(checkstack)-z-1] == '(':
                        incompletescore += 1
                    elif checkstack[len(checkstack)-z-1] == '[':
                        incompletescore += 2
                    elif checkstack[len(checkstack)-z-1] == '{':
                        incompletescore += 3
                    elif checkstack[len(checkstack)-z-1] == '<':
                        incompletescore += 4
                incompletescores.append(incompletescore)
                break
        elif checkstack[len(checkstack)-1] == '{':
            if x[y] == '}':
                checkstack.pop()
            elif x[y] == ')':
                print("Expected }, found )")
                errorscore += 3
                break
            elif x[y] == ']':
                print("Expected }, found ]")
                errorscore += 57
                break
            elif x[y] == '>':
                print("Expected }, found >")
                errorscore += 25137
                break
            if y == len(x)-1 and len(checkstack) != 0:
                print("Incomplete")
                for z in range(0,len(checkstack)):
                    incompletescore *= 5
                    if checkstack[len(checkstack)-z-1] == '(':
                        incompletescore += 1
                    elif checkstack[len(checkstack)-z-1] == '[':
                        incompletescore += 2
                    elif checkstack[len(checkstack)-z-1] == '{':
                        incompletescore += 3
                    elif checkstack[len(checkstack)-z-1] == '<':
                        incompletescore += 4
                incompletescores.append(incompletescore)
                break
        elif checkstack[len(checkstack)-1] == '<':
            if x[y] == '>':
                checkstack.pop()
            elif x[y] == ')':
                print("Expected >, found )")
                errorscore += 3
                break
            elif x[y] == ']':
                print("Expected >, found ]")
                errorscore += 57
                break
            elif x[y] == '}':
                print("Expected >, found }")
                errorscore += 1197
                break
            if y == len(x)-1 and len(checkstack) != 0:
                print("Incomplete")
                for z in range(0,len(checkstack)):
                    incompletescore *= 5
                    if checkstack[len(checkstack)-z-1] == '(':
                        incompletescore += 1
                    elif checkstack[len(checkstack)-z-1] == '[':
                        incompletescore += 2
                    elif checkstack[len(checkstack)-z-1] == '{':
                        incompletescore += 3
                    elif checkstack[len(checkstack)-z-1] == '<':
                        incompletescore += 4
                incompletescores.append(incompletescore)
                break

incompletescores.sort()

print("Error Score: " + str(errorscore))
print("Incomplete Score: " + str(incompletescores[int(len(incompletescores)/2)]))