# Description: This program removes duplicates from an array

# Function to remove duplicates from an array
def removeDuplicates(nums):
    dup = []
    for i in range(len(nums)-1):
        if nums[i] not in dup:
            dup.append(nums[i])
    return dup

#main
nums = [1, 3, 5, 6, 3, 5, 6, 1]
dup=removeDuplicates(nums)

print(dup)