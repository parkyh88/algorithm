import sys

n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().strip().split(" ")))
# answer = []

# for i in range(n):
#   nge = n_arr.pop(0)
    
#   if len(n_arr) == 0:
#     answer.append(-1)
    
#   for j in range(len(n_arr)):
#     if nge < n_arr[j]:
#       answer.append(n_arr[j])
#       break
#     else:
#       if len(n_arr)-1 == j:          
#         answer.append(-1)

# print(" ".join(str(val) for val in answer))
stack = []
answer = [0] * n

for i in range(n):
  while stack and n_arr[stack[-1]] < n_arr[i]:
    answer[stack.pop()] = n_arr[i]  
  stack.append(i)

if len(stack) != 0:
  for val in stack:
    answer[val] = -1

print(" ".join(str(val) for val in answer))


for i in range(n):
  if len(stack) == 0:
    stack.append(i)
  else:
    for j in range(len(stack)):
      if n_arr[stack[-1]] < n_arr[i]:
        answer.append(n_arr[i])
        stack.pop()            
    
    stack.append(i)    
  
  if i == n-1:
    answer.append(-1)
    stack.pop()    
    
if len(stack) != 0:
  for val in stack:
    answer.insert(val, -1)

print(" ".join(str(val) for val in answer))