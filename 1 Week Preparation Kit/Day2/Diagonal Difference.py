def diagonalDifference(arr):
    main_diagonal = 0
    secondry_diagonal = 0
    for i in range(len(arr)):
        main_diagonal += arr[i][i]
        secondry_diagonal += arr[i][len(arr) - i - 1]
    return abs(main_diagonal - secondry_diagonal)
print(diagonalDifference([[11,2,4], [4,5,6], [10,8,-12]]))