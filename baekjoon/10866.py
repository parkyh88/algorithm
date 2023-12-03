#import sys

# n = int(sys.stdin.readline())
# cli_arr = []

# for i in range(n):
#   cli = sys.stdin.readline().strip().split(" ")
  
#   if cli[0] == "push_front":
#     cli_arr.insert(0, cli[1])
  
#   if cli[0] == "push_back":
#     cli_arr.append(cli[1])
    
#   if cli[0] == "pop_front":    
#     print(cli_arr.pop(0) if len(cli_arr) != 0 else "-1")
  
#   if cli[0] == "pop_back":
#     print(cli_arr.pop() if len(cli_arr) != 0 else "-1")
    
#   if cli[0] == "size":
#     print(len(cli_arr))
    
#   if cli[0] == "empty":
#     print("0" if len(cli_arr) != 0 else "1")
    
#   if cli[0] == "front":
#     print( cli_arr[0] if len(cli_arr) != 0 else "-1")   

#   if cli[0] == "back":
#     print( cli_arr[-1] if len(cli_arr) != 0 else "-1")  
  
#-------------------------------------------------------
from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
  cli = sys.stdin.readline().strip().split(" ")
  
  if cli[0] == "push_front":
    deq.appendleft(cli[1])
  
  if cli[0] == "push_back":
    deq.append(cli[1])
    
  if cli[0] == "pop_front":    
    print(deq.popleft() if len(deq) != 0 else "-1")
  
  if cli[0] == "pop_back":
    print(deq.pop() if len(deq) != 0 else "-1")
    
  if cli[0] == "size":
    print(len(deq))
    
  if cli[0] == "empty":
    print("0" if len(deq) != 0 else "1")
    
  if cli[0] == "front":
    print( deq[0] if len(deq) != 0 else "-1")   

  if cli[0] == "back":
    print( deq[-1] if len(deq) != 0 else "-1")  
  