from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) < 2:
            if scoville[0] < K:
                answer = -1
            break
        a = heappop(scoville)
        b = heappop(scoville)
        
        heappush(scoville, a+(b*2))
        answer += 1
    
        
    return answer