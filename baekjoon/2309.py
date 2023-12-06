import sys

n = 9
n_arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]

# for i in range(n):
#   h = int(sys.stdin.readline())
#   n_arr.append(h)
  
count = 0
for i in range(n):  
  for j in range(i, n):
    count += n_arr[j] 
  
  print(count)
  count = 0
  