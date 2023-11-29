import sys

def sumFn(a, b):
  return (a+b)*(a-b)
  
a, b = map(int, sys.stdin.readline().split(" "))
print(sumFn(a,b))