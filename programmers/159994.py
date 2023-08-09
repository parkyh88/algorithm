def solution(cards1, cards2, goal):
    check_goal = []
    for word in goal:
        if word in cards1:
            check_index = cards1.index(word)
            if check_index != 0:
                return "No"
            else:
                check_goal.append(word)
                cards1.pop(0)
        
        if word in cards2:
            check_index = cards2.index(word)
            if check_index != 0:
                return "No"    
            else:
                check_goal.append(word)
                cards2.pop(0)
            
    return "Yes"