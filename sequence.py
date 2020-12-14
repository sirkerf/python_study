n,m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0: dp[i][j] = i+j
        else:
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+cost)
print(dp[n][m])