from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    
    while True:
        if len(truck_weights) == 0 and current_weight == 0:
            break
        answer += 1
        current_weight -= bridge.popleft()
        if len(truck_weights) >= 1:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
    
    return answer