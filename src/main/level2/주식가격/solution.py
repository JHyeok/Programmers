def solution(prices):
    answer = [0] * len(prices)
    
    # 가격이 떨어지지 않은 기간은 몇 초인지 계산.
    # 탈출 조건을 세우는게 중요한 거 같다. 탈출 조건은 가격이 떨어졌을 때,
    cnt = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break

        answer[i] = cnt
        cnt = 0

    return answer


# 다른 사람의 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer