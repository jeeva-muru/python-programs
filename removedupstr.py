# function that removes all occurrences of a given character from a string.
def removeChars(sname, val):      
    for i in range(len(val)):
        sname = sname.replace(val[i], "")
    return sname

name = "jeeva"
sname = removeChars(name,"j")
print(sname)