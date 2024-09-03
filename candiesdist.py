# https://leetcode.com/problems/distribute-candies/description/

def distribute():
    eat = ()
    for i in candies:
        if i not in eat:
            eat += (i,)
    print(eat)

candies = [1,1,2,3]
distribute()