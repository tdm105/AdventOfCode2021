import split

file = open("Day10/input.txt","r")
input = file.readlines()

for x in range(0,len(input)):
    if input[x][len(input[x])-1] == '\n':
        input[x] = input[x][:len(input[x])-1]

errorscore = 0

for x in input:
    checkstack = []
    for y in range(1,len(x)):
        if x[y-1] == '[' or x[y-1] == '<' or x[y-1] == '{' or x[y-1] == '(':
            checkstack.append(x[y-1])
        if len(checkstack) == 0:
            if y == len(x)-1:
                break
        elif checkstack[len(checkstack)-1] == '[':
            if y == len(x)-1:
                break
            elif x[y] == ']':
                checkstack.pop()
            elif x[y] == ')':
                errorscore += 3
                break
            elif x[y] == '}':
                errorscore += 1197
                break
            elif x[y] == '>':
                errorscore += 25137
                break
        elif checkstack[len(checkstack)-1] == '(':
            if y-1 == len(x)-1:
                break
            elif x[y] == ')':
                checkstack.pop()
            elif x[y] == ']':
                errorscore += 57
                break
            elif x[y] == '}':
                errorscore += 1197
                break
            elif x[y] == '>':
                errorscore += 25137
                break
        elif checkstack[len(checkstack)-1] == '{':
            if y-1 == len(x)-1:
                break
            elif x[y] == '}':
                checkstack.pop()
            elif x[y] == ')':
                errorscore += 3
                break
            elif x[y] == ']':
                errorscore += 57
                break
            elif x[y] == '>':
                errorscore += 25137
                break
        elif checkstack[len(checkstack)-1] == '<':
            if y-1 == len(x)-1:
                break
            elif x[y] == '>':
                checkstack.pop()
            elif x[y] == ')':
                errorscore += 3
                break
            elif x[y] == ']':
                errorscore += 57
                break
            elif x[y] == '}':
                errorscore += 1197
                break

print("Error Score: " + str(errorscore))