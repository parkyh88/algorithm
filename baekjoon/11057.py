n = int(input())
dp = [1] * 10

for i in range(2, n+1):
  for j in range(10):
    print(dp)
    dp[j] = sum(dp[j:])
    
print(dp)