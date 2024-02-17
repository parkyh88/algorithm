n, b = map(int, input().split(" "))
answer = []
while True:
  check = n % b  
  if check >= 10:
    ord_chr = check+55
    answer.append(chr(ord_chr))
  else:
    answer.append(str(check))
    
  n = n // b  
  if n <= 0:
    break
  
print("".join(str(answer[i]) for i in range(len(answer)-1,-1,-1)))