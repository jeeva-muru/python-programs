
# Function to rotate the array to the right by k elements
def rotateright(arr1, k):
    print(arr1[k:])
    print(arr1[:k])
    arr1 = arr1[k:] + arr1[:k]
   
    print("The array after rotating by", k, "elements is:", arr1)

# Function to rotate the array to the left by k elements
def rotateleft(arr, k):
    arr = arr[-k:] + arr[:-k]
    print("The array after rotating by", k, "elements is:", arr)

def rotateright1(arr, k):
    for i in range(k):
        element = arr.pop()
        arr.insert(0,element)

    print("The array after rotating by", k, "elements is:", arr)

def rotateleft1(arr, k):
    print(arr)
    for i in range(k):
        element = arr.pop(0)
        print(element)
        arr.append(element)
        # print(arr)

    print("The array after rotating by", k, "elements is:", arr)

#main
arr = [ 1,2,3,4,5,6,7]
k = 2
rotateright1(arr, k) # [6, 7, 1, 2, 3, 4, 5]
rotateleft1(arr, k) # [3, 4, 5, 6, 7, 1, 2]