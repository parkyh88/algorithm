import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().strip().split(" ")))
v = int(sys.stdin.readline())

count = 0
for val in n_arr:
  if val == v:
    count += 1
    
print(count)