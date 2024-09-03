def removeElement(nums, val):
    # i = 0
    # for j in range(len(nums)):
    #     if nums[j] != val:
    #         nums[i] = nums[j]
    #         i += 1
    # return i
    # print("nums", len(nums))
    # for i in range(len(nums)-1):
    #     print("i", i)
    #     if nums[i] == val:
    #         nums.pop(i)

    while val in nums:
        nums.remove(val)


nums = [1,2,3,2,4,3,3]
k = 3
print(removeElement(nums, k))
print(nums)