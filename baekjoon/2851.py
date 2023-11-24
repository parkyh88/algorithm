import sys

mushroom = 10
prefix_sum = [0] * int(mushroom+1)

for idx in range(1, mushroom+1):
  score = int(sys.stdin.readline())
  prefix_sum[idx] = prefix_sum[idx-1] + score
    
  if prefix_sum[idx] >= 100:
    pre_check = 100 - prefix_sum[idx-1]
    next_check = prefix_sum[idx] - 100
    
    if pre_check == next_check:
      print(prefix_sum[idx])
    elif pre_check < next_check:
      print(prefix_sum[idx-1])
    else:
      print(prefix_sum[idx])      
    break
  
  if idx == mushroom and prefix_sum[len(prefix_sum)-1] < 100:
    print(prefix_sum[len(prefix_sum)-1])
