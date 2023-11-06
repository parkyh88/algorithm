def solution(citations):
    # 논문 총 편 수
    len_citations = len(citations)
    
    # 오름차순으로 정렬을 해서 순서대로 진행, 몇 회 인용 되었는 데, 인용된 횟수와 편의 개수가 같아야한다.
    sort_citations = sorted(citations)    
   
    for idx in range(len_citations+1):
        first_count = 0
        second_count = 0
        
        for citation in sort_citations:            
            if idx < citation:
                first_count += 1     
                
            if idx <= citation:
                second_count += 1    
                
        if first_count == idx:
            return first_count      
        
        if second_count == idx:
            return second_count