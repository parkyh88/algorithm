def solution(survey, choices):
    standard = 4                
    preData = ''
    answer = ''
    character_list = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0,
    }
    
    for idx, data in enumerate(survey):
        choice = choices[idx]
        
        if int(choice) > int(standard):
            character_list[data[1]] = int(character_list[data[1]]) + int(choice) - int(standard)
        else:
            character_list[data[0]] = int(character_list[data[0]]) + int(standard) - + int(choice)

    for idx, data in enumerate(character_list):        
        if int(idx+1) % 2 == 0:
            if int(character_list[preData]) < int(character_list[data]):
                answer += data 
            else:
                answer += preData
        else:
            preData = data
        
    return answer