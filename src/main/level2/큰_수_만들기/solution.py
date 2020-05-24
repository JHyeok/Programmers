import itertools

# 테스트 케이스에서 시간초과 발생
def fail_solution(number, k):
    answer = ''
    # 몇 개로 조합을 할 것인지 number - k
    permutation_criteria = len(number) - k
    
    num_list = list(itertools.combinations(number, permutation_criteria))
    max_list = max(num_list)

    for i in max_list:
        answer += i

    return answer

param1 = "1231234"
param2 = 3

print(solution(param1, param2)) # return 3234

# "1924" 에서 두개의 수를 제거하면 19, 12, 14, 92, 94, 24를 만들 수있다.
# 이 중 가장 큰 숫자는 94이다.
# 배열을 만든 다음에 max 함수를 사용하면 최고 값을 구할 수 있다.
# k는 1이상 number의 자릿수 미만인 자연수

# 배운 점
# 순열과 조합의 차이를 알게됨, 이 문제는 조합을 이용해야 함
# 그런데 조합으로 풀었을 때, 몇 몇 테스트 케이스에서 시간 초과 오류가 발생

# 다른 사람의 풀이를 참고하였음
# 참고: https://gurumee92.tistory.com/180
def solution(number, k):
    collected = []

    for x in number:
        while collected and collected[-1] < x and k > 0:
            collected.pop()
            k -= 1
        
        collected.append(x)

    # 방법1
    # while k > 0:
    #     collected.pop()
    #     k -= 1

    # 방법2
    collected = collected[:-k] if k > 0 else collected

    answer = "".join(collected)
    return answer