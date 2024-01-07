def gcd(n, m):
  if n % m == 0:
    return m
  else:
    return gcd(m, n%m)

t = int(input())

for i in range(t):  
  n_arr = list(map(int, input().split(" ")))
  answer = 0
  for i in range(1, n_arr[0]):
    for j in range(i+1, n_arr[0]+1):
      answer += gcd(n_arr[i], n_arr[j])
      
  print(answer)