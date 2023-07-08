def solution(babbling):
    check_babbling = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for char in babbling:
        if len(char) <= 1:
            continue
        else:
            for check_char in check_babbling:
                if char.find(check_char*2) != -1:                
                    continue

                if char.find(check_char) != -1:
                    char = char.replace(check_char, "O")              
            
            if 'O'*len(char) in char:
                result += 1
                
    return result
                