# import sys

# s = sys.stdin.readline()
# q = int(sys.stdin.readline())
# s_arr = [ s[idx] for idx in range(len(s)-1) ]
# c_arr = []

# def soultion(c_arr, i, j):
#   answer = 0
  
#   for idx in range(i, j+1):
#     answer += c_arr[idx]

# for idx in range(q):
#   a, i, j = sys.stdin.readline().split(" ")
  
#   if idx == 0:
#     for char in s_arr:
#       if char == a:            
#         c_arr.append(1)
#       else:
#         c_arr.append(0)   
         
#     soultion(c_arr, int(i), int(j))    
#   else:
#     soultion(c_arr, int(i), int(j))
import sys

s = list(sys.stdin.readline())
ord_count = 97
alphabet_count = 26
s_arr = [[0] * alphabet_count for _ in range(len(s)+1)]

for i in range(1, len(s_arr)):
    for j in range(alphabet_count):
        if ord(s[i-1])-ord_count == j:
            s_arr[i][j] = s_arr[i-1][j] + 1
        else:
            s_arr[i][j] = s_arr[i-1][j]

q = int(sys.stdin.readline())
for idx in range(q):
    a, i, j = sys.stdin.readline().split(" ")
    a, i, j = ord(a)-ord_count, int(i), int(j)
    print(s_arr[j+1][a]-s_arr[i][a])