import sys

# n, m = map(int, (sys.stdin.readline().split(" ")))
# x_arr = list(map(int, (sys.stdin.readline().split(" "))))

n = 4
m = 2
x_arr = [1, 1, 1, 1]
prefix_sum = [0] * int(len(x_arr)+1)

for i in range(1, len(x_arr)+1):
  prefix_sum[i] = prefix_sum[i-1] + x_arr[i-1]

count = 0
for i in range(n):
  for j in range(i+1, n+1):
    print(i, j)
    if prefix_sum[j] - prefix_sum[i] == m:
      count += 1
      
print(count)


