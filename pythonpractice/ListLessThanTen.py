def getElementsLessThan(nums, k):
    vals = filter(lambda x : x < k, nums)
    #vals = filter(lambda x : x < 5, nums)
    print(*vals, sep=",")

getElementsLessThan([1,2,6,4,10,12,14,2], 4)