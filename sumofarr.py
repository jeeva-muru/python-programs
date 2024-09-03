# def arraySum(arr, val):
#     length = len(arr)-1
#     for i in range(length):
#         for j in range(i+1, length):
#             if((arr[i]+arr[j])==val):
#                 return True
        
        
# arr=[3,5,4,7,9]
# val=10
# result=arraySum(arr, val)
# if(result):
#     print("true")
# else:
#     print("false")

def arrayProblem(arr, val):
    length = len(arr)-1
    for i in range(length):
        for j in range(i+1,length):
            if((arr[i]+arr[j])==val):
                return True
                
arr=[2,5,4,7,9]
val=10
result=arrayProblem(arr, val)
if(result):
    print("true")
else:
    print("false")