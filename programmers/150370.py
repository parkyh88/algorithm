def timestamp_create(year, month, day):
    timestamp_today = (int(year) * 12 * 28) + (int(month) * 28) + (int(day))    
    return timestamp_today
        
def solution(today, terms, privacies):
    # timestamp로 비교
    year, month, day = today.split('.')
    timestamp_today = timestamp_create(year, month, day)
    terms_obj = { data.split(' ')[0] : data.split(' ')[1]  for data in terms }
    answer = []
    
    
    for idx, data in enumerate(privacies):
        p_date, p_type = data.split(' ')        
        p_year, p_month, p_day = p_date.split('.')
        timestamp_p = timestamp_create(p_year, p_month, p_day) + (int(terms_obj[p_type]) * 28)
        
        if int(timestamp_p) <= int(timestamp_today):
            answer.append(idx+1)
    
    return answer
                
        