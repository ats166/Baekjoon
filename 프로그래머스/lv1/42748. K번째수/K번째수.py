def solution(array, commands):
    answer = []
    result = []
    
    for i in range(len(commands)): 
        answer = array[:commands[i][1]]
        answer = answer[commands[i][0]-1:]
        answer.sort()
        answer = answer[commands[i][2]-1]
        result.append(answer)
    
    
    
    return result