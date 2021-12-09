def split(str,chr):
    newstr = []
    lastloc = 0
    for x in range(0,len(str)):
        if str[x] == chr:
            newstr.append(str[lastloc:x])
            lastloc = x+1
    return newstr
    