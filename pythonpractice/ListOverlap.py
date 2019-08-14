def getOverlap(nums1, nums2):
    return set(nums1).intersection(set(nums2))

nums1 = [1,2,3,4,5]
nums2 = [3,4,5]
print(*getOverlap(nums1, nums2), sep=",")