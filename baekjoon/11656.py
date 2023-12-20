s = input()
answer = []
for i in range(len(s)):  
  answer.append(s[i:len(s)])
  
for val in sorted(answer):
  print(val)