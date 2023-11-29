import sys
t = int(sys.stdin.readline())

def sum(a, b):
  return a+b

for i in range(t):
  a, b = map(int, sys.stdin.readline().split(" "))
  print(sum(a, b))