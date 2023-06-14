from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(begin)
    level = 0
    q = deque([(begin, level)])
    if target in words:
        while q:
            now = q.popleft()
            if now[0] == target:
                answer = now[1]
                break

            for word in words:
                cnt = 0
                path = [False] * n
                for i in range(n):
                    if now[0][i] == word[i]:
                        path[i] = True
                for j in range(n):
                    if path[j] == False:
                        cnt += 1
                if cnt == 1:
                    q.append((word, now[1]+1))
    else:
        answer = 0
    
    return answer