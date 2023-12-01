import sys

left_stack = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
right_stack = []

for i in range(m):
  cli = sys.stdin.readline().strip().split(" ")

  if cli[0] == 'L':    
    if left_stack != []:
      left = left_stack.pop()
      right_stack.append(left)

  if cli[0] == 'D':
    if right_stack != []:
      right = right_stack.pop()
      left_stack.append(right)

  if cli[0] == 'B':
    if left_stack:
      left_stack.pop()
    
  if cli[0] == 'P':
    left_stack.append(cli[1])
   
print("".join(left_stack)+"".join( right_stack[j] for j in range(len(right_stack)-1, -1, -1)))

# for i in range(m):
#   cli = sys.stdin.readline().strip().split(" ")
#   cli_len = len(cli)
    
#   if (cli[0] == 'L' or cli[0] == 'B') and cursor == 0:
#     continue
  
#   if cli[0] == 'D' and cursor == len(n_str):
#     continue
  
#   if cli[0] == 'L':
#     cursor -= 1  
#   elif cli[0] == 'B':
#     cursor -= 1
#     del n_str[cursor]        
#   elif cli[0] == 'D':
#     cursor += 1
#   else:        
#     n_str.insert(cursor, cli[1])
#     cursor += 1
  
# print("".join(n_str))