import sys

while True:
  try:    
    a, b = map(int, sys.stdin.readline().split(" "))    
    print(a+b)    
  except Exception as err:
    break