def minSumPath(A):

    memo = [None] * len(A)
    n = len(A) - 1

    for i in range(len(A[n])):
        memo[i] = A[n][i]

    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[i])):
            memo[j] = A[i][j] + min(memo[j],
                                    memo[j + 1]);

    return memo[0]

A = [[2],
     [3, 9],
     [1, 6, 7]]
print(minSumPath(A))

