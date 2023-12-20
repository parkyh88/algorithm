from collections import deque

def solution(prices):
    stack_prices = deque(prices)
    answer = []
    
    while stack_prices:
        count = 0
        price = stack_prices.popleft()
        print("price : ", price)
        
        for val in stack_prices: 
            print("val", val)
            count += 1
            if price > val:
                break    
            
        print(count)        
                
        answer.append(count)
    
    print(answer)
        
    
solution([1, 2, 3, 2, 3])