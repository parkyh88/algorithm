import math

n = int(input())
n_arr = list(map(int, input().split(" ")))
answer = 0

# for val in n_arr:
#   tmp = []
#   cnt = 1
#   while True:
#     if val < cnt:
#       break
#     else:
#       if val % cnt == 0:
#         tmp.append(cnt)              
#       cnt += 1
    
#   if len(tmp) == 2:
#     answer += 1

# print(answer)


def primenum(val):
  if val == 1:
    return False
  
  for i in range(2, int(math.sqrt(val))+1):
    if val % i == 0:
      return False
  
  return True   

for val in n_arr:  
  check = primenum(val)
  
  if check:
    answer += 1 
          
print(answer)
      
    
  

      
