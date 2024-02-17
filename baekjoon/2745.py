n, b = input().split(" ")
answer = 0
count = 0

for i in range(len(n)-1, -1, -1):
  if n[i].isalpha():
    sys_n = int(ord(f'{n[i]}') - 55)
  else:
    sys_n = int(n[i])
        
  answer += (sys_n * (int(b)**count))
  count += 1

print(answer)