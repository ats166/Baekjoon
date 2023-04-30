def solution(citations):
    max = 0
    citations.sort()

    for i in range(citations[-1]+1):
        low,high = 0, 0
        for j in range(len(citations)):
            if citations[j] >= i:
                high += 1
            else:
                low += 1
        if low <= i and high >= low and i <= high:
            max = i

    return max