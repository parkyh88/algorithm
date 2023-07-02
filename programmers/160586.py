def solution(keymap, targets):
  answer = []
  keymap_obj = {}
  
  for keys in keymap:
    for idx, key in enumerate(keys):
      if key not in keymap_obj:
        keymap_obj[key] = int(idx) + 1
      else:
        keymap_obj[key] = min(int(keymap_obj[key]), int(idx + 1))


  for idx, target in enumerate(targets):
    count = 0
    for char in target:
      if char not in keymap_obj:
        count = -1
        break
      else:
        count = count + keymap_obj[char]
            
    answer.append(count)
    

  return answer