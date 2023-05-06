def solution(nums):
    answer = 0
    n = len(nums) // 2
    ponketmon = {}
    
    for i in range(len(nums)):
        try:
            ponketmon[nums[i]] += 1
        except:
            ponketmon[nums[i]] = 1
            
    if n <= len(ponketmon):
        answer = n
    else:
        answer = len(ponketmon)
    
    
    return answer