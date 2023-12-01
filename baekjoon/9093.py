import sys

t = int(sys.stdin.readline())
for m in range(t):
  t_arr = list(sys.stdin.readline().split(" "))
  answer = ""
  for j, t_str in enumerate(t_arr):
    t_str = t_str.split("\n")[0]  
    for i in range(len(t_str)-1, -1, -1):    
      answer += t_str[i]
    
    answer += "" if j == len(t_arr) else " "
    
  print(answer)