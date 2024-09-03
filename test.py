import array as arr

def fact(n):
    result = 0
    for i in range(1, n):
     result += result * i
     fact(i)

def numgen():
    i =0
    for i in range(1000000):
        yield i

val: int = 5
name: str = "Jeeva"
list = [1, 2, "muru", 4, "5"]
numbers = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
array = arr.array('i', [1, 2, 3, 4, 5])
array1 = arr.array('i', numbers)
for index in range(len(array1)):
    print(array1[index])
length = len(array1.tolist())
# for i in range(len(array1)):
#      print(array1[i])
# print(min(list))
print(list[2:])
print(list[:2])
print(list[0::2])
# print(array.append("6"))

# generator = numgen()
# print(next(generator))
# print(next(generator))