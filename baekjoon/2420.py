import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))

if n >= m:
  print(n-m)
else:
  print(m-n)