
# Problem: Lemonade Change, LeetCode 860
def billchange():
    fivebills = 0
    tenbills = 0
    twentybills = 0
    for bill in bills:
        if bill == 5:
            fivebills += 1
        elif bill == 10:
            tenbills += 1
            fivebills -= 1
        else:
            twentybills += 1
            if tenbills > 0 and fivebills > 0:
                tenbills -= 1
                fivebills -= 1
            elif fivebills >=3:
                fivebills -= 3
            else:
                return False
    return True

# bills = [5, 5, 5, 10, 20]
bills=[5,5,10,10,5]
print(billchange())