def stringleftover(str1, str2):
    # str1 = list(str1)
    str2 = list(str2)
    for i in str2:
        str1=str1.replace(i, "")
    # return "".join(str1)
    print(str1)
    return str1

def removerepeated(str1):
    # str1 = list(str1)
    str2 = []
    for i in str1:
        if i not in str2:
            str2.append(i)
    return "".join(str2)
    # return str2


str1 = "AABBBCCDDD"
str2 = "AB"
print(stringleftover(str1, str2)) # CCDD
print(removerepeated(str1)) # ABCD