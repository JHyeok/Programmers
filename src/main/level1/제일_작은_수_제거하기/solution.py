def solution(arr):
    answer = []

    if len(arr) <= 1:
        answer.append(-1)
        return answer

    min_num = min(arr)

    for num in arr:
        if min_num < num:
            answer.append(num)
    
    return answer

    # 다시 Python으로 푸는데 제한조건을 빼먹었다. 제한조건에 같은 수가 나올 수 없다고 하였으니 remove로 그냥 제거만 해줘도 된다.
    # 나는 작은 수가 여러개 나오는 경우를 생각해서 answer에 가장 작은 수보다 큰 수들만 append 해주었다.