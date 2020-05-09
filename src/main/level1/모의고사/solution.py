def solution(answers):
    answer = []

    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(0, len(answers)):
        if people1[i%len(people1)] == answers[i]:
            score[0] += 1
        if people2[i%len(people2)] == answers[i]:
            score[1] += 1
        if people3[i%len(people3)] == answers[i]:
            score[2] += 1

    best_score = max(score)
    for i in range(0, len(score)):
        if score[i] == best_score:
            answer.append(i + 1)

    return answer

# 반복문 사용시 enumerate를 사용하면 인덱스 번호도 같이 알 수 있다.
# >>> t = [1, 5, 7, 33, 39, 52]
# >>> for p in enumerate(t):
# ...     print(p)
# ... 
# (0, 1)
# (1, 5)
# (2, 7)
# (3, 33)
# (4, 39)
# (5, 52)

# enumerate를 적용한 다른 사람의 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result