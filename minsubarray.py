
# Given an array of integers and a target value, return the minimum contiguous subarray 
# that sums up to the target value. If there are multiple subarrays with the same sum, return the one that starts from the beginning of the array.
def minimumSizeSubarray(nums, target):

    length = len(nums)
    finalArray=[]
    # for i in range(length-1):
    #     # for j in range(i+1,length):
    #     if((nums[i]+nums[i+1])==target):
    #         return nums[i],nums[i+1]
    #     elif(nums[i]==target):
    #         return nums[i]
    sum=0
    for i in range(0,length):
        sum=nums[i]
        print("i",i)
        for j in range(i+1,length):
            sum = sum + nums[j]
            print("sum",sum)
            if(sum == target):
                return nums[i:j+1]
            elif(nums[i]==target):
                return nums[i]        

nums = [1,5,4,7,4,3]
target = 14
result = minimumSizeSubarray(nums, target)
print(result) # return (1,5) or (5,1) 