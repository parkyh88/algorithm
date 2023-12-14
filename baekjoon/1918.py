s = input()
stack = []
answer = ""

for char in s:  
  if char not in ('*','/', '(', ')', '+', '-'):
    answer += char  
  else:
    if char == '(':
      stack.append(char)
    elif char == "*" or char == "/":
      while stack and ( stack[-1] == "*" or stack[-1] == "/"):
        answer += stack.pop()      
      stack.append(char)
    elif char == "+" or char == "-":
      while stack and stack[-1] != "(":
        answer += stack.pop()      
      stack.append(char)
    elif char == ")":
      while stack and stack[-1] != "(":
        answer += stack.pop()  
      stack.pop()
   
while stack:
  answer += stack.pop()
  
print(answer)


#char.isalpha()
# for i in range(len(s)):
#   while stack and ( s[stack[-1]] == "*" or s[stack[-1]] == "/" or s[i] == ")" ):
#     if s[i] == "*" or s[i] == "/":      
#       answer[i] = s[stack.pop()]
#       answer[i-1] = s[i]
#       answer[i-2] = s[stack.pop()]    
#     elif s[i] == "+" or s[i] == "-":
#       answer[i] = s[stack.pop()]
#       answer[]
    
          
    
#   stack.append(i)

# print(answer)
    
