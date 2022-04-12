if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    for elem in range(n - 1, -1, -1):
        print(arr[elem], end=' ')