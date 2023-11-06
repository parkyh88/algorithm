def solution(n, left, right):
    check_arr = []
    left_n = int(left / n)+1
    right_n = int(right / n)+1
    range_left = left-((left_n-1)*n)
    range_right = range_left + (right-left) + 1
       
    for idx1 in range(left_n, right_n+1):
        for idx2 in range(1, n+1):
            if idx1 >= idx2:
                check_arr.append(idx1)
            else:
                check_arr.append(idx2)   
            
    return  check_arr[range_left:range_right]