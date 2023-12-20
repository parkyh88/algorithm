s = input()
rot13 = 13
upper_ored = 122
lower_ord = 90
answer = ""

for char in s:
  if char == " ":
    answer += char
  elif char.isalpha():
    ord_char = ord(char)
    if ord_char >= 97:
      if ord_char+rot13 > upper_ored:
        answer += chr((ord_char + rot13) - upper_ored + 96)
      else:
        answer += chr(ord_char + rot13)
    else:
      if ord_char+rot13 > lower_ord:
        answer += chr((ord_char + rot13) - lower_ord + 64)
      else:
        answer += chr(ord_char + rot13)     
  else:
    answer += char 
    
print(answer)