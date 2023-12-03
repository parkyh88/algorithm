import sys

t = int(sys.stdin.readline())

for i in range(t):
  r, s = sys.stdin.readline().strip().split(" ")
  answer = ""
    
  for j in range(len(s)):
    answer += s[j] * int(r)
    
  print(answer)