a, b = input().split(" ")
a_reverse = "".join( a[i] for i in range(len(a)-1, -1, -1))
b_reverse = "".join( b[i] for i in range(len(b)-1, -1, -1))

print( int(a_reverse) if int(a_reverse) > int(b_reverse) else int(b_reverse))