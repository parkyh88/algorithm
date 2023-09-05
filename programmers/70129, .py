def solution(s):
    zero_count = 0
    binary_count = 0
    
    while int(s) > 1:    
        zero_len = s.count('0')        
        len_s = len(s)  
        #s = bin(len('1' * (len_s - zero_len))).split('0b')[1]
        s = bin(len_s - zero_len).split('0b')[1]
        zero_count += zero_len
        binary_count += 1

    return [binary_count, zero_count]