# 처음 제출하고 시간 초과 뜬 코드
# 질문하기를 보니 itertools를 사용하면 시간복잡도가 O(n!)이라서 그럴 것 같다고 한다.
def solution(numbers):
    import itertools
    
    answer = ''

    # itertools.permutation를 사용해서 순열
    # 숫자 배열을 문자열 배열로 바꾸기 (순열 사용하기 쉽게)
    numbers = list(map(str, numbers))
    all_list = list(map(''.join, itertools.permutations(numbers, len(numbers))))
    
    answer = str(max(all_list))
    return answer


def fix_solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # sort의 기준이 x * 3 인 이유는,
    # 각 num의 자릿수가 1000 이하이기 때문이다.
    # 가령 [9, 991] 이면 9에다가 *2 해도 99, 991991로 991이 앞편에 정렬이지만
    # *3을 하면 999, 991991991로 9가 앞편에 정렬되기 때문이다.
    numbers.sort(key=lambda x: x*3, reverse=True)
    # str, int는 '0000' 같은 걸 '0'으로 바꾸기 위해 작성
    # ''.join(numbers)로 하면 테스트 케이스12 오류 발생
    answer = str(int(''.join(numbers)))

    # 문자열 비교연산의 경우에는 첫번째 인덱스인 666[0]의 6과, 101010[0]인 1과 222[0]인 2를 ascii 숫자로 바꿔서 비교하며
    # 같으면 다음 인덱스도 비교한다.
    return answer