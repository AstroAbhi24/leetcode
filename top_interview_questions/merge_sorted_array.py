def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    nums1[m:] = nums2
    nums1.sort()
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6,7,2,3], 6))