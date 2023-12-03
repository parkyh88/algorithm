import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))
n_arr = [ i for i in range(1, n+1) ]
cursor = 0
answer = []

while len(n_arr) > 0:    
  cursor += k - 1
  if cursor >= len(n_arr):
    cursor %= len(n_arr)
        
  answer.append(n_arr.pop(cursor))  
  
print('<'+', '.join(str(val) for val in answer)+'>')