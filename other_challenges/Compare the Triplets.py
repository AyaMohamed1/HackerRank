def compareTriplets(a, b):
    result = [0,0]
    for x in range(0, 3):
        if a[x] > b[x]:
            result[0] += 1
        elif a[x] < b[x]:
            result[1] += 1
    return result
print(compareTriplets([5,6,7], [3,6,10]))