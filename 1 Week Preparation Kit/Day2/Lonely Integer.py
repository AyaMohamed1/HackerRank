def lonelyinteger(a):
    occurs = [0] * 110
    for i in range(len(a)):
        occurs[a[i]] += 1
    for i in range(len(a)):
        if occurs[a[i]] == 1:
            return a[i]
print(lonelyinteger([1,2,3,4,3,2,1]))