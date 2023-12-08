import sys

n = int(sys.stdin.readline())
answer = []

for i in range(n):
  number = int(sys.stdin.readline())
  if i != 0:
    if (answer[i-1] < number):
      answer.append()
    else:
      answer.insert(0, number)
  else:
    answer.append()
  
for val in answer:
  print(val)