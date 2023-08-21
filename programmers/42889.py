def solution(N, stages):
    len_stages = len(stages)    
    check_arr = {}
    count_stages = { stage: 0 for stage in stages }    

    for stage in stages:        
        count_stages[stage] += 1

    for idx in range(1, N+1):   
        if idx in count_stages.keys():
            check_arr[idx] = (count_stages[idx] / len_stages) * 100 
            len_stages = len_stages - count_stages[idx]
        else:
             check_arr[idx] = 0

    return sorted(check_arr, key=lambda x: check_arr[x], reverse=True)