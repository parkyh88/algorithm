n = int(input())
m = input()
count = 1
answer = 0
for i in range(2, -1, -1):
  multi = n * int(m[i])
  print(multi)
  answer += multi * count
  count *= 10

print(answer) 