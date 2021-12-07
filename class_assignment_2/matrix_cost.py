def matrix_algo_sub(p, i, j, dp):
    if(i == j):
        dp[i][j] = 0
        return 0
    if(dp[i][j] != -1):
	    return dp[i][j]
    dp[i][j] = float('inf')
    for k in range(i,j):
	    dp[i][j] = min(dp[i][j], matrix_algo_sub(p,i,k,dp) + matrix_algo_sub(p,k + 1,j,dp)+ (p[i - 1] * p[k] * p[j]))
    return dp[i][j]

def Matrix_Mul(p):
    n = len(arr)
    i = 1
    j = n - 1
    dp = [[-1 for i in range(n)] for j in range(n)]
    cost = matrix_algo_sub(p,i,j,dp)
    return dp,cost

arr = [10, 100, 20, 5, 80]
solutions,min_cost = Matrix_Mul(arr)
for sol in solutions:
    print(sol)
print("Minimum Cost: ",min_cost)