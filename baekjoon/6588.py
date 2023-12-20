# import sys
# import math

# arr = [ True ] * 1000001
# while True:
#   n = int(sys.stdin.readline())  
#   if n == 0:
#     break
  
#   for i in range(2, int(math.sqrt(n))+1):
#     if arr[i] == True:
#       j = 2      
#       while i * j <= n:
#         arr[i*j] = False
#         j += 1

#   is_prime = []
#   for i in range(3, n+1):
#     if arr[i] and arr[i] % 2 == 1: 
#       is_prime.append(i)
    
#   answer = []
#   for i in range(len(is_prime)):
#     for j in range(i+1, len(is_prime)):
#       if len(answer) == 0:
#         if is_prime[i] + is_prime[j] == n:        
#           answer.append(is_prime[i])
#           answer.append(is_prime[j])
#       else:
#         break
      
#   if not answer:
#     print("Goldbach's conjecture is wrong.")
#   else:
#     print(f"{n} = {answer[0]} + {answer[1]}") 
import sys
import math

arr = [ True ] * 1000001

for i in range(2, int(math.sqrt(1000000)+1)):
  if arr[i] == True:
    for j in range(i+i, 1000001, i):
      arr[j] = False

while True:
  n = int(sys.stdin.readline())  
    
  if n == 0:
    break
  else:
    check = 0
    for i in range(3, 1000001):
      if arr[i] and arr[n-i]:
        print(f"{n} = {i} + {n-i}")
        check = 1
        break
    
    if check == 0:
      print("Goldbach's conjecture is wrong.")