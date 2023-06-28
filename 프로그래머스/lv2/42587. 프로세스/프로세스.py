def solution(priorities, location):
    answer = 0
    rank = [0] * len(priorities)
    a = 1
    while True:
        if min(rank) != 0:
            break
        
        for i in range(len(priorities)):
            if max(priorities) == priorities[i] and max(priorities) != 0:
                rank[i] = a
                priorities[i] = 0
                a += 1
    
    return rank[location]