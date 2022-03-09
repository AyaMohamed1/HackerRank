def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        positive += 1 if num > 0 else 0
        negative += 1 if num < 0 else 0
        zero += 1 if num == 0 else 0
    print("{:.6f}".format(positive / len(arr)))
    print("{:.6f}".format(negative / len(arr)))
    print("{:.6f}".format(zero / len(arr)))
    # return [positive, negative, zero]

plusMinus([1,1,0,-1,-1])