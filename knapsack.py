def knapsack(N, W, weight, value):
    inf = float("inf")
    dp = [[-inf for i in range(W+1)] for j in range(N+1)]
    for i in range(W+1):
        dp[0][i]=0
    
    for i in range(N):
        for w in range(W+1):
            if weight[i]<w:
                dp[i+1][w]=max(dp[i][w-weight[i]] + value[i], dp[i][w])
            else:
                dp[i+1][w]=dp[i][w]
    return dp[N][W]