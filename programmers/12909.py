def solution(s):
    l_bracket = 0
    r_bracket = 0
    
    for idx in range(len(s)):
        if s[idx] == '(':
            l_bracket += 1            
        else:
            if l_bracket >= 1:
                l_bracket -= 1
            else:
                r_bracket += 1
    
    return True if l_bracket == 0 and r_bracket == 0 else False