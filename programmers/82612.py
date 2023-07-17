def solution(price, money, count):
    result = sum([ price*(idx+1) for idx in range(count) ]) - money  
    return 0 if result <= 0 else result