import sys

n = int(sys.stdin.readline())
n_arr = []
answer = []
count = 1

for i in range(n):
  a = int(sys.stdin.readline())
  print(count)
  while count <= a:
    n_arr.append(count)
    answer.append("+")
    count += 1
    
  if n_arr[-1] == a:
    answer.append("-")
    n_arr.pop()

if len(n_arr) == 0:
  print("\n".join(answer))  
else:
  print("NO") 