import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().strip().split(" ")))
f_stack = {}

for i, val in enumerate(n_arr):
  if val in f_stack.keys():
    f_stack[val] += 1
  else:
    f_stack[val] = 1
    
ngf_stack = []
answer = [0] * n

for i, val in enumerate(n_arr):  
  while ngf_stack and f_stack[n_arr[ngf_stack[-1]]] < f_stack[val]:   
    answer[ngf_stack.pop()] = val
                
  ngf_stack.append(i)
  
if ngf_stack:
  for val in ngf_stack:
    answer[val] = -1
    
print(" ".join(str(val) for val in answer))