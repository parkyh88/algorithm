n = int(input())
fact = 1
cnt = 0

for i in range(1, n+1):
  fact *= i
  
fact = str(fact)

for i in range(len(fact)-1, -1, -1):
  if fact[i] == "0":
    cnt += 1
  else:
    break

print(cnt)