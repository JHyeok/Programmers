from collections import deque


def solution(priorities, location):
    answer = 1
    queue = deque()

    # 중요도와 위치를 같이 저장해서 큐를 만든다
    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    while True:
        if max(priorities) > queue[0][0]:
            queue.append(queue[0])
            queue.popleft()
        else:
            # location과 queue의 위치가 일치하면 몇 번째로 인쇄되는지 return 한다
            if location == queue[0][1]:
                return answer
            
            # 원래 순서대로 빠졌기 때문에 중요도는 0으로 초기화해주고 몇 번째로 인쇄되는지는 1 올려준다
            # 큐에서 삭제되었기 때문에 이 위치는 이제 더 이상 if문에서 비교하지 않는다
            priorities[queue[0][1]] = 0
            queue.popleft()
            answer += 1