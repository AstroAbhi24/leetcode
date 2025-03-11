def removeElement(nums: list[int], val: int) -> int:
    l = 0
    while l<len(nums):
        if nums[l]==val:
            nums.pop(l)
        else:
            l+=1
    return len(nums)

print(removeElement([1,2,3,4,5,6,7,8,5,9,10], 5))