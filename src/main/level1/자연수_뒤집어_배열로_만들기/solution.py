# 처음 제출한 코드
def solution(n):
    answer = []

    num_list = list(str(n))

    for i in range(len(num_list) - 1, -1, -1):
        answer.append(int(num_list[i]))

    return answer

# 다른 사람의 풀이
def other_solution(n):
    return list(map(int, reversed(str(n))))

# 다른 풀이를 보고 처음 제출한 코드를 개선
def solution(n):
    answer = []

    num_list = list(str(n))
    num_list.reverse()
    answer = list(map(int, num_list))

    return answer