def miniMaxSum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0
    for num in range(0, len(arr) - 1):
        min_sum += arr[num]
    for num in range(1, len(arr)):
        max_sum += arr[num]
    print(min_sum, end=" ")
    print(max_sum)
miniMaxSum([5,2,1,4,3])