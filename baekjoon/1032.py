import sys

n = int(sys.stdin.readline())
n_arr = list(sys.stdin.readline().split("\n")[0])

for i in range(n-1):
  check_arr = list(sys.stdin.readline().split("\n")[0])
  for j in range(len(n_arr)):
    if n_arr[j] != check_arr[j]:
      n_arr[j] = "?"
      
print("".join(n_arr))      
