n, m = map(int, input().split(" "))
answer = [ 0 ] * n

for l in range(m):
  i, j, k = map(int, input().split(" "))
  
  for o in range(i-1, j):
    answer[o] = k
    
print(" ".join(str(val) for val in answer))