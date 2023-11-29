import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split(" ")))
prefix_sum = 0
result = 0

for i in range(n-1, 0, -1):  
  prefix_sum += n_arr[i]
  
  result += n_arr[i-1] * prefix_sum
    
print(result)