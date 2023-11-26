import sys

n, s = map(int, sys.stdin.readline().split(" "))
n_arr = list(map(int, sys.stdin.readline().split(" ")))

left, right = 0, 0
answer = 100001
n_sum = n_arr[0]

while left <= right:  
  print(right, left)
  if n_sum >= s:    
    n_sum -= n_arr[left]
    answer = min(answer, right-left+1)    
    left += 1
  else:
    right += 1
    if right < n:
      n_sum += n_arr[right]   
    else:
      break

if answer == 100001:
  answer = 0
  
print(answer)