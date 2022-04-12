T = int(input().strip())
for test in range(0, T):
    S = input()
    even_indexed = ''
    odd_indexed = ''
    for idx in range(0, len(S)):
        if idx % 2:
            odd_indexed += S[idx]
        else:
            even_indexed += S[idx]
    print(even_indexed, odd_indexed)