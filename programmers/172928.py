def solution(park, routes):
    max_w = len(park[0])
    max_h = len(park)
    start_point = []
    coordinate_obj = {"N" : [-1, 0],  "E": [0, 1],  "S" : [1, 0], "W" : [0, -1]}
    
    for i in range(max_h):
        for j in range(max_w):
            if park[i][j] == "S":
                start_point = [i, j]         
    
    for route in routes:
        direction, step = route.split(' ')
        x, y = coordinate_obj[direction]
        next_x, next_y = start_point[0],  start_point[1]
        
        for idx in range(int(step)):            
            next_x, next_y = int(x + next_x), int(y + next_y)  
            
            if 0 <= next_x < max_h and 0 <= next_y < max_w:
                if park[next_x][next_y] == "X":
                    break
        
        if 0 <= next_x < max_h and 0 <= next_y < max_w:   
             if park[next_x][next_y] != "X":                    
                start_point = [next_x, next_y]

    
    return start_point
    
    
    
    