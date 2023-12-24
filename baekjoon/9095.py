n = int(input())
dp = [0, 1, 2, 4] + [0] * (7)

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for j in range(n):
  t = int(input())
  print(dp[t])