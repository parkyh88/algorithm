import sys

n = int(sys.stdin.readline())
answer = {}

for i in range(n):
  age, name = sys.stdin.readline().strip().split(" ")  
  answer[f"{int(age)}"] = []
  
  
print(answer)
    
    
  
  
  