def staircase(n):
    for i in range(0, n):
        for j in range(i+1, n):
            print(' ', end='')
        for j in range(0, i+1):
            print('#', end='')
        print()
staircase(5)