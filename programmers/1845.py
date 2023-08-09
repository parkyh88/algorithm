def solution(nums):
    nums_count = int(len(nums) / 2)
    set_nums = len(list(set(nums)))    
    return nums_count if set_nums >= nums_count else set_nums