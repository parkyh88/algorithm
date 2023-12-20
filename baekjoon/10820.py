while True:
  try:
    n = input()
    n_arr = [0, 0, 0, 0]
    answer = ""
    
    for char in n:
      if char.isalpha():
        if ord(char) >= 97:
          n_arr[0] += 1
        else:
          n_arr[1] += 1        
      elif char == " ":
        n_arr[3] += 1
      else:
        n_arr[2] += 1
    
    answer = " ".join(str(val) for val in n_arr)          
    print(answer)
    
  except Exception as err:
    break