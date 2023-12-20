s = input()
s_obj = { f"{i}" : -1 for i in range(26)}
answer = ""

for i, char in enumerate(s):
  key = ord(char)-97  
  if s_obj[f"{key}"] == -1:
    s_obj[f"{key}"] = i
    
for val in s_obj.values():
  answer += f"{val} "  

print(answer)