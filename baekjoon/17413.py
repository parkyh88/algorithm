import sys

s = list(sys.stdin.readline().strip())
s_arr = []
temp_str = ""

for i in range(len(s)):   
  if "<" == s[i]:
    if len(temp_str) != 0:
      s_arr.append(temp_str)
    temp_str = ""
    temp_str += s[i]
  
  elif ">" == s[i]:
    temp_str += s[i]
    s_arr.append(temp_str)
    temp_str = ""
  
  elif " " == s[i]:    
    s_arr.append(temp_str)  
    s_arr.append(" ")
    temp_str = ""
  else:  
    if i == len(s)-1 and len(temp_str) != 0:
      temp_str += s[i]
      s_arr.append(temp_str)
    else:
      temp_str += s[i]
      
answer = []
check = False
len_s_arr = len(s_arr)

for i in range(len_s_arr):
  for j in range(len(s_arr[i])):
    if "<" == s_arr[i][j]:
      check = True
            
    if not check:
      answer.append(s_arr[i][len(s_arr[i])-j-1])
    else:
      answer.append(s_arr[i][j])   
      
    if ">" == s_arr[i][j]:
      check = False 
      
print("".join(answer))
    
