def solution(board, moves):
  doll_location = { i+1 : [] for i in range(len(board)) }
  doll_arr = []
  result = 0
  
  for i in range(len(board)): 
    for j in range(len(board[i])):
      if board[i][j] != 0:
        doll_location[j+1] = [board[i][j]] + doll_location[j+1]

  for move in moves:        
    doll_len = len(doll_location[move])
    if doll_len != 0:
      if len(doll_arr) != 0:                   
        if doll_arr[-1:][0] == doll_location[move][doll_len-1:][0]:
          result += 2
          doll_arr.pop()
          doll_location[move].pop()
        else:
          doll_arr.append(doll_location[move][doll_len-1:][0])
          doll_location[move].pop()
      else:
        doll_arr.append(doll_location[move][doll_len-1:][0])
        doll_location[move].pop()
  
  return result