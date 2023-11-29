import sys

n, k = map(int, sys.stdin.readline().split(" "))
n_arr = list(map(int, sys.stdin.readline().split(" ")))

limit_max = -9999
for i in range(n-k+1):
  limit_max = max(limit_max, sum(n_arr[i:i+k]))
  
print(limit_max)

#-----------------------------------------------
import sys

n, k = map(int, sys.stdin.readline().split())
n_arr = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(n_arr[:k]))

for i in range(n-k):
  result.append(result[i] - n_arr[i] + n_arr[k+i])

print(max(result))