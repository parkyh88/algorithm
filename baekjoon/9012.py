import sys

t = int(sys.stdin.readline())

for i in range(t):
  t_arr = list(sys.stdin.readline().split("\n")[0])
  count = 0
  for ps in t_arr:
    if count == 0 and ps == ")":
      count = -1
      break
            
    if ps == "(":
      count += 1
    else:
      count -= 1
  
  print("YES" if count == 0 else "NO")