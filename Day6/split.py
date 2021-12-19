def split(str,chr):
    newstr = []
    lastloc = 0
    for x in range(len(chr),len(str)):
        if str[x-len(chr):x] == chr:
            newstr.append(str[lastloc:x-len(chr)])
            lastloc = x
    newstr.append(str[lastloc:])
    return newstr
    