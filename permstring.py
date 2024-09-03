# https://leetcode.com/problems/permutation-in-string/description/
import re as regex

def permutationstring():
    #local variables
    length2 = len(str2)
    ch = str2[0]
    str3 = "muru"
    print(str3)
    # for ch in str2:
    print(str1.index(ch))
    index = str1.index(ch)
    if index+length2 < len(str1):
        filtered1 = str1[index:index+length2]
    else:
        filtered1 = str1[index:]
    print("filtered1-",filtered1)


    found = True
    if length2 == len(filtered1):
        for ch in filtered1:
            if ch not in str2:
                found =  False
                break
    else:
        found = False

    if not found:
        if index+length2-1 < len(str1):
            print("in1")
            filtered2 = str1[index-length2+1:index+length2]
        else:
            print("in")
            filtered2 = str1[index-length2+1:]
            print("filtered2-", filtered2)

        if length2 == len(filtered2):
            for ch in filtered2:
                print("next")
                if ch not in str2:
                    found = False
                    break
                else:
                    found = True
    return found
    
    
if __name__ == '__main__':  
    # global variables
    str1 = "murubca"
    str2 = "abc"
    str3 = "cba"
    print(permutationstring())
    print(str3)
   