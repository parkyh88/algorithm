import sys

n, m = map(int, sys.stdin.readline().split(" "))
n_arr = list(map(int, sys.stdin.readline().split(" ")))

n_sum_arr = [0] * (len(n_arr)+1)

for idx in range(1, len(n_sum_arr)):
  n_sum_arr[idx] = n_sum_arr[idx-1] + n_arr[idx-1]

for idx in range(m):
  i, j = map(int, sys.stdin.readline().split())  
  print(n_sum_arr[j] - n_sum_arr[i-1])