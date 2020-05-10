def solution(arrangement):
    answer = 0
    stack = []
    
    for s in arrangement:
        if (s == "("):
            stack.append(0)
            last = s
        else:
            stack.pop()
            if (last == "("):
                answer = answer + len(stack)
                last = s
            else:
                answer += 1
    
    return answer