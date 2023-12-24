student = { i : False for i in range(1, 31)}

for i in range(1, 29):
  n = int(input())
  student[n] = True
  
for i, val in student.items():
  if val == False:
    print(i)