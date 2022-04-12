def birthdayCakeCandles(candles):
    max_candel = max(candles)
    sum = 0
    for c in candles:
        if c == max_candel:
            sum += 1
    return sum
print(birthdayCakeCandles([3, 2, 1, 3]))