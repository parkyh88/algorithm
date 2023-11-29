import sys

n, x = map(int, sys.stdin.readline().split(" "))
n_arr = list(map(int, sys.stdin.readline().split(" ")))
answer = " ".join(str(num) for num in n_arr if x > num)
print(answer)
