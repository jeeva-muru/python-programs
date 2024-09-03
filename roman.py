def convert():
    numstr = str(num)
    romanstr=''
    
    if (len(numstr)==1):
        number=int(numstr[0])
        romanstr += roman[number-1]
        # print(romanstr)
    else:
        for n in range(0, len(numstr), 1 ):
            # print("n", n)
            #first digit
            if (n == 0):
                for i in range(int(numstr[n])):
                    romanstr += roman[9]
                    # print(romanstr)
            else:
                number=int(numstr[n])
                romanstr += roman[number-1]
                # print(romanstr)
    
    return romanstr

def int_to_roman(num):
    roman_num = ''  
    i = 0
    while num > 0:
        # print(i, num, val[i])
        for _ in range(num // val[i]):
            print("i", i, "num", num, "val[i]", val[i])
            roman_num += roman1[i]
            num -= val[i]
        i += 1

    return roman_num

roman = ['I', 'II', 'III', 'IV', 'V','VI', 'VII','VIII', 'IX', 'X']
roman1 = ['I', 'V','X']
val = [  10, 9, 5, 4,
         1]
print("hi")
num=0
while (True):
    num = int(input("enter one number: "))
    if (num==0):
        break
    # result = convert()
    result = int_to_roman(num)
    print(result)