n = int(input())
p = [0] + list(map(int, input().split(" ")))
dp = [0] * (n+1)

for i in range(1, n+1):
  for j in range(1, n+1):
    if j-i >= 0:
      dp[j] = max(dp[j], dp[j-i] + p[i])
            
print(dp[n])