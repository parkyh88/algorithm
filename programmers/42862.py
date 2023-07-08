def solution(n, lost, reserve):
    reserve_arr = sorted([ data for data in reserve if data not in lost ])
    lost_arr = sorted([ data for data in lost if data not in reserve ])
    result = n
    
    if len(lost_arr) > 0 or len(reserve_arr) > 0:
        for data in reserve_arr:
            if data - 1 in lost_arr:
                lost_arr.remove(data-1)
                continue

            if data + 1 in lost_arr:
                lost_arr.remove(data+1)
                continue
    
    result = result - len(lost_arr)
        
    return result