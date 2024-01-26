s = input()
check_s = "".join( s[i] for i in range(len(s)-1, -1, -1))

if s == check_s:
  print("1")
else:
  print("0")