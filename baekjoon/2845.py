l, p = map(int, input().split(" "))
n_arr = list(map(int, input().split(" ")))
check_person = l * p
answer = []

for val in n_arr:
  answer.append(val-check_person)
  
print(" ".join( str(val) for val in answer))