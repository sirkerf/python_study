def part_sum0(a,A):
    N=len(a)
    dp = [[0 for i in range(A+1)]for j in range(N+1)]
    dp[0][0]=1

    for i in range(N):
        for j in range(A+1):
            if a[i] <= j:
                dp[i+1][j]=dp[i][j-a[i]] or dp[i][j]
            else:
                dp[i+1][j]=dp[i][j]
    return dp[N][A]