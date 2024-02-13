n = int(input())
answer = []

while True:   
  if n == 0:
    answer.append(0)
    break
  
  if n == 1:
    answer.append(1)
    break
  
  if n % 2 == 0:
    answer.append(0)
    n = n // -2
  else:
    answer.append(1)
    n = (n // -2) + 1

print("".join(str(answer[i]) for i in range(len(answer)-1, -1, -1)))
