import math
# 방학기간
l = int(input())
# 국어 총 페이지
a = int(input())
# 수학 총 페이지
b = int(input())
# 국어 하루 최대 처리 페이지
c = int(input())
# 수학 하루 최대 처리 페이지
d = int(input())

check_arr = [ math.ceil(b / d), math.ceil(a / c) ] 
answer = l - max(check_arr)
print(answer)