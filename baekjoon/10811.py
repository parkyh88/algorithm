n, m = map(int, input().split(" "))
answer = [ i for i in range(1, n+1) ]

for k in range(m):
  i, j = map(int, input().split(" "))
  check_arr = []
  for t in range(j-1, i-2, -1):
    check_arr.append(answer[t])  
    
  answer[i-1:j] = check_arr
  
print(" ".join(str(val) for val in answer))