from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0 # 시간
    truck_bridge = deque() # 다리 위의 트럭
    truck_bridge_location = deque() # 다리 위의 트럭 위치
    truck_weights = deque(truck_weights)
    N = len(truck_weights)

    while True:
        # 다리 위의 트럭이 없고, 대기하고 있는 트럭이 없다면
        if len(truck_bridge) == 0 and len(truck_weights) == 0:
            return answer

        # 시간 증가
        answer += 1

        # 트럭이 움직인 거리 증가
        for i in range(len(truck_bridge)):
            truck_bridge_location[i] += 1

        if len(truck_bridge) != 0:
            if truck_bridge_location[0] == bridge_length:
                truck_bridge.popleft()
                truck_bridge_location.popleft()
        if len(truck_weights) != 0:
            if sum(truck_bridge) + truck_weights[0] <= weight:
                truck_bridge.append(truck_weights[0])
                truck_bridge_location.append(0)
                truck_weights.popleft()

    return answer