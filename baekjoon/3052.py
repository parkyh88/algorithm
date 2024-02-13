answer = []
for i in range(10):
  n = int(input())
  answer.append(n%42)
  
print(len(set(answer)))