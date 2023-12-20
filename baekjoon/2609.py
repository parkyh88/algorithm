#일반론
n, m = map(int, input().split(" "))
count = 2
share = []
remain = 0
answer = 1

while True:  
  if n < count or m < count:
    for val in share:
      answer *= val      
      
    remain = answer * n * m
    break 
    
  if n % count == 0 and m % count == 0:    
    share.append(count)
    n = n // count
    m = m // count
  else:
    count += 1  
    
print(answer)
print(remain)

# 유클리드 호제법 활용
n, m = map(int, input().split(" "))
remain = (n*m)
while m != 0:
  [n, m] = [ m, n%m ]
  
print(n)
print(int(remain / n))