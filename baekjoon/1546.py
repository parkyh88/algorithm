import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().strip().split(" ")))
max_n = max(n_arr)
answer = []

for val in n_arr:
  answer.append(val/max_n*100)
  
print(sum(answer)/n)