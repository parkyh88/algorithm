import sys

n = int(sys.stdin.readline())
cli = sys.stdin.readline().strip()
stack = []
n_arr = []
count = 0

for i in range(n):
  n_arr.append(int(sys.stdin.readline()))

for val in cli:
  if val.isalpha():      
    stack.append(n_arr[ord(val)-65])
  else:   
    if val == '*':  
      top = stack.pop()
      pre = stack.pop()          
      stack.append(pre*top)      
    elif val == "/":    
      top = stack.pop()
      pre = stack.pop()          
      stack.append(pre/top)  
    elif val == "+":
      top = stack.pop()
      pre = stack.pop()          
      stack.append(pre+top)  
    else:
      top = stack.pop()
      pre = stack.pop()          
      stack.append(pre-top)    

print(f"{stack[0]:.2f}")