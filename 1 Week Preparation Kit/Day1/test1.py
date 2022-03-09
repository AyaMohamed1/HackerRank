def findMedian(arr):
    arr.sort()
    return (arr[int(len(arr) / 2)])
print(findMedian([3,2,7,1,4,6,5]))