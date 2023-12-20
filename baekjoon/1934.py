t = int(input())

def lcm(a, b):
  while b != 0:
    [a, b] = [b, a % b]
  
  return a

for i in range(t):
  a, b = map(int, input().split(" "))
  answer = (a * b) / lcm(a, b)
  print(int(answer))