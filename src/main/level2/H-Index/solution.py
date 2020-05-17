# 문제 이해가 어려웠다.
# 테스트 케이스 9, 11이 실패해서 질문하기에서 테스트 케이스가 무엇인지 확인하고 풀었다.
# 테스트 케이스 16 - [0, 0, 0, 0] / return 0
# [2, 2, 2, 2, 2] / return 2
# [5, 5, 5, 5] / return 4
# 제출한 코드
def solution(citations):
    citations.sort()
    answer = citations[0]

    cnt = 0 
    for i in range(0, len(citations)):
        for j in citations:
            if j >= i:
                cnt += 1
            if cnt == i:
                answer = cnt
        if i !=0 and i == answer:
            answer = cnt
        cnt = 0

    return answer

# 다른 사람의 풀이
def solution(citations):
    citations.sort()
    citations_len = len(citations)

    for i in range(citations_len):
        if citations[i] >= citations_len - i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return citations_len - i

    return 0

# 다른 사람의 풀이2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0