from collections import Counter

def solution(players, callings):
    play_check = {player: i for i, player in enumerate(players)}
    idx_play_check = {i:player for i, player in enumerate(players)}

    for data in callings:
        # 현재 선수의 위치
        now_idx = play_check[data]
        # 현재 선수 앞의 선수 위치
        pre_idx = now_idx-1
        
        # 현재 선수가 앞에 등수로 바뀌고, 앞에 선수가 뒷 등수가 된다.
        play_check[data] = pre_idx  
        play_check[idx_play_check[pre_idx]] = now_idx
        
        idx_play_check[now_idx] = idx_play_check[pre_idx]
        idx_play_check[pre_idx] = data
        

    return list(idx_play_check.values())