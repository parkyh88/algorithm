def solution(numbers, hand):    
  standard = 12
  numbers_location = {}
  left_default_location = [1, 4, 7]
  right_default_location = [3, 6, 9]
  left_location = [0, 3]
  right_location = [2, 3]
  x_count = 0
  y_count = 0
  result = []

  for idx in range(standard):    
    if idx !=0 and int(idx) % 3 == 0:
      x_count = 0
      y_count = y_count + 1            
      numbers_location[idx+1] = [x_count, y_count]
      x_count = x_count + 1
    else:
      if idx+1 != 11:
        numbers_location[idx+1] = [x_count, y_count]
        x_count = x_count + 1
      else:
        numbers_location[0] = [x_count, y_count]
        x_count = x_count + 1


  for number in numbers:        
    move_finger = numbers_location[number]      
    if number in left_default_location:
      left_location = move_finger
      result.append('L')            
    elif number in right_default_location:
      right_location = move_finger
      result.append('R')   
    else:    
      x_move_0 = (move_finger[0] - left_location[0]) if (move_finger[0] - left_location[0]) > 0 else -(move_finger[0] - left_location[0])
      y_move_1 = (move_finger[1] - left_location[1]) if (move_finger[1] - left_location[1]) > 0 else -(move_finger[1] - left_location[1])      
      x_move_1 = (move_finger[0] - right_location[0]) if (move_finger[0] - right_location[0]) > 0 else -(move_finger[0] - right_location[0])
      y_move_2 = (move_finger[1] - right_location[1]) if (move_finger[1] - right_location[1]) > 0 else -(move_finger[1] - right_location[1])                
      left_move_count =  x_move_0 + y_move_1
      right_move_count = x_move_1 + y_move_2

      if left_move_count == right_move_count:
        hand_upper = hand[:1].upper()
        if hand_upper == 'R':
          result.append(hand_upper)
          right_location = move_finger                   
        else:
          result.append(hand_upper)
          left_location = move_finger
      elif left_move_count > right_move_count:
        right_location = move_finger
        result.append('R')
      else:
        left_location = move_finger
        result.append('L')


    answer = ''.join(result)
    return answer