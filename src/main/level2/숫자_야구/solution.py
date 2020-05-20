# 다른 사람의 풀이를 참고하였음
# 참고: https://gurumee92.tistory.com/180
def get_score(request, number):
    strike, ball = 0, 0

    for i in range(3):
        if request[i] == number[i]:
            strike += 1
        elif request[i] in number:
            ball += 1

    return strike, ball

def solution(baseball):
    answer = 0
    possible_answer = []

    # 123 - 987 까지 각 자릿수가 겹치지 않는 숫자들
    numbers = [str(i) for i in range(1, 10)]
    baseball_num = [
        numbers[i] + numbers[j] + numbers[k]
        for i in range(9)
        for j in range(9)
        for k in range(9)
        if i != j and j != k and i !=k
    ]

    for request, strike, ball in baseball:
        baseball_num = [number for number in baseball_num if get_score(str(request), number) == (strike, ball)]

    answer = len(baseball_num)
    return answer

# 123 - 987 까지 각 자릿수가 겹치지 않는 숫자들

# 스트라이크
# request[i] == possible_answer[i]

# 볼 (해당 숫자는 존재하지만, 자릿수는 일치하지 않음)
# request[i] != possible_answer[i] && request[i] in possible_answer

# 123 - 987 까지 각 자릿수가 겹치지 않는 숫자들은 itertools.permutations를 사용해서도 만들 수 있다. (순열)
# list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))

# 야구 게임에 답으로 나올 수 있는 모든 숫자들
# 이 숫자들을 baseball을 순회하면서 get_score 함수를 만들어서 같은 스트라이크, 볼이 나오는 숫자들로 재구성
# 마지막에 남은 숫자들을 가지고 길이를 반환
def solution(baseball):
    from itertools import permutations
    numbers = [ str(x) for x in range(1, 10) ] 
    candidates = [ ''.join(result_set) for result_set in permutations(numbers, 3) ]
    
    for (request, strikes, balls) in baseball:
        candidates = [ number for number in candidates if get_score(str(request), number) == (strikes, balls) ]
    
    answer = len(candidates)
    return answer