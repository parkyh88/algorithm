import math

m, n = map(int, input().split(" "))
arr = [ True ] * int(n+1)

for i in range(2, int(math.sqrt(n))+1):
  if arr[i] == True:
    j = 2
    while i * j <= n:
      arr[i*j] = False
      j += 1

for i in range(m, n+1):
  if arr[i]:
    if i != 1:
      print(i)



# def gcd(i):
#   if i == 1:
#     return False
  
#   for j in range(2, int(math.sqrt(i))+1):
#     if i % j == 0:
#       return False
  
#   return True

# for i in range(m, n+1):
#   check_gcd = gcd(i)
#   if check_gcd:
#     answer.append(i)
  
# for val in answer:
#   print(val)