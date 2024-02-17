n = list(map(int, (input().split(" "))))
n.sort()
print(" ".join( str(val) for val in n))