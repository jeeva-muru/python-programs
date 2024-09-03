
# Reverse a string using for loop and slicing
def reverse(str):
    for ch in range(len(str)-1, -1, -1):
        print(str[ch], end="")

#Reverse a string using slicing
def reverse1(str):
    print(str[::-1])

reverse("jeeva murugesan")
reverse1("jeeva murugesan")