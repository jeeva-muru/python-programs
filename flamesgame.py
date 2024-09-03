
# Function to find the relationship status
def flames(uname: str, pname: str):
    for ch in uname:
        if ch in pname:
            uname = uname.replace(ch, "", 1)
            pname = pname.replace(ch, "", 1)

    count = len(uname) + len(pname)
    print("count: ", count)
    print("uname: ", uname)
    print("pname: ", pname)
    index = 0
    for i in range(len(flames) - 1):
        index = (index + count - 1) % len(flames)
        print("index: ", index)
        print("Removed: ", flames[index])
        flames.remove(flames[index])

    status = flamesDesc[flames.index(flames[0])]
    return status

    


# main
flames = ['F', 'L', 'A', 'M', 'E', 'S']
flamesDesc = ["Friend", "Love", "Affection", "Marriage", "Enemy", "Sister"]
uname = input("Enter your name: ")
pname = input("Enter your partner's name: ")
status = flames(uname, pname)
print("Relationship status: ", status)