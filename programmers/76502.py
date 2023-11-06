def solution(s):
    len_s = len(s)
    list_s = list(s)
    check_arr = []
    char_check_obj = { ']' : '[', '}' : '{', ')' : '('} 
    first_check_arr = [']', '}', ')']
    last_check_arr = ['[', '{', '(']
    count = 0
    
    for idx in range(len_s):
        if list_s[0] in first_check_arr or list_s[len_s-1] in last_check_arr:            
            pass
        else:            
            for idx2 in range(len(list_s)):
                if idx2 == 0:
                    check_arr.append(list_s[idx2])
                else:                    
                    if list_s[idx2] in last_check_arr:
                        check_arr.append(list_s[idx2])
                    else:
                        if len(check_arr) != 0 and check_arr[len(check_arr)-1] == char_check_obj[list_s[idx2]]:  
                            check_arr.pop()
                        else:
                            check_arr.append(list_s[idx2])  
                
            if len(check_arr) == 0:
                count += 1
                
            check_arr = []
                
                
        list_s.append(list_s[0])
        list_s.pop(0)
        
    return count
        
    