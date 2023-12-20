s = input()
s_obj = { f"{i}" : 0 for i in range(26)}
answer = ""
for char in s:
  key = ord(char)-97
  s_obj[f"{key}"] += 1

for val in s_obj.values():
  answer += f"{val} "
  
print(answer)