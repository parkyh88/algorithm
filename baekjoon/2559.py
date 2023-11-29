import sys

n, k = map(int, sys.stdin.readline().split())
k_arr = list(map(int, sys.stdin.readline().split()))

result = []
result.append(sum(k_arr[:k]))

for i in range(n-k):
  result.append(result[i] - k_arr[i] + k_arr[k+i])

print(max(result))