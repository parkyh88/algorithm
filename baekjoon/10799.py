import sys

n = sys.stdin.readline()
stack = []
answer = 0

for i, char in enumerate(n):    
  if char == "(":
    stack.append(i)
  
  if char == ")":
    if stack:
      pop = stack.pop()    
      if i - pop == 1:        
        answer += len(stack)
      else:      
        answer +=  1
  
print(answer)