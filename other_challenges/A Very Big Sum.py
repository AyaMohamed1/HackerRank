def aVeryBigSum(ar):
    sum = 0
    for elm in ar:
        sum += elm
    return sum
print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))