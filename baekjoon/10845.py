import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
  cli = sys.stdin.readline().strip().split(" ")
  
  if cli[0] == 'push':
    queue.append(cli[1])
  
  if cli[0] == 'pop':
    if len(queue) != 0:
      print(queue.pop(0))
    else:
      print("-1")      
  
  if cli[0] == 'size':
    print(len(queue))
    
  if cli[0] == 'empty':
    print('1' if len(queue) == 0 else '0')
    
  if cli[0] == 'front':
    if len(queue) != 0:
      print(queue[0])
    else:
      print("-1")
  
  if cli[0] == 'back':
    if len(queue) != 0:
      print(queue[-1])      
    else:
      print("-1")