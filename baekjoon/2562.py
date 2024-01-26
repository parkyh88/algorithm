n_arr = []

while True:
  try:
    n = int(input())
    n_arr.append(n)
  except Exception as Err:
    break

print(max(n_arr))
print(n_arr.index(max(n_arr))+1)