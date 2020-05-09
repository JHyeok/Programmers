# 처음 제출한 코드
def solution(participant, completion):
    answer = ''

    list.sort(participant)
    list.sort(completion)
    completion.append(-1)

    for idx, people in enumerate(participant):
        if idx != len(participant):
            if people != completion[idx]:
                answer = people
                return answer
        else:
            answer = participant[len(participant)]
            return answer
    
    return answer

# 테스트 케이스는 전부 통과했지만 내가 생각해도 이상한 코드
# 제출하고 나니 participant[len(participant)] 는 오류가 발생하는 코드

# 다른 사람의 풀이
def other_solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

# 정말 기발한 다른 사람의 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 다른 풀이를 보고 처음 제출한 코드를 개선
def solution(participant, completion):
    answer = ''

    list.sort(participant)
    list.sort(completion)

    for i in range(0, len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    
    answer = participant[len(participant) - 1]
    return answer