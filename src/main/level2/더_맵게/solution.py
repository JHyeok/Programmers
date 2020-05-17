# 처음 제출한 코드
# 3, 8, 14 테스트 케이스가 계속해서 실패
def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville_list = []

    while True:
        for i in scoville:
            if i < K:
                scoville_list.append(i)

        # 탈출 조건
        if len(scoville_list) == 0:
            break
        
        if len(scoville_list) < 2:
            answer += 1
            break

        m_K = scoville_list[0] + (scoville_list[1] * 2)

        if m_K > K:
            scoville_list[0] = K + 1
            scoville_list[1] = K + 1
        else:
            scoville_list[0] = K + 1
            scoville_list[1] = m_K

        answer += 1
        scoville_list.sort()
        scoville = []
        scoville = scoville_list
        scoville_list = []

    if len(scoville_list) == 1:
        scoville.sort()
        m_K = scoville_list[0] + (scoville[0] * 2)
        if K > m_K:
            answer = -1

    return answer

param1 = [1, 2, 3, 9, 10, 12]
param1 = 7
print(solution(param1, param2)) # return 2

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 스코빌 지수를 교체하면 List 가 변경된다. 그리고 answer +=  1 된다.
# 스코빌 지수 계산에 쓰이는 값들은 리스트에서 삭제 처리.

# 1. K보다 작은 숫자들을 구하고 그걸 list로 만든다?
# 2. 리스트로 만들어진 상태에서 이제 스코빌 지수를 구하고 그 값으로 리스트를 새로 만든다.
# 3. 그리고 answer +=1 해준다.
# 4. 새로만든 리스트에서 다시 위에 1번을 반복한다.

# 3, 8, 14 테스트 케이스가 계속해서 실패하고, 힙 관련 문제는 처음이라 답지를 확인
# 확인해보니 대부분 heapq 모듈을 사용해야 한다고 적혀있다.
# 그리고 나 처럼 무식하게 돌리는 방법과 리스트를 새로 만드는 방법보다는 min 을 이용해서 최소값을 구하고
# 그 최소값을 K와 비교하는 방법과 큐를 만들어서 pop(0) 해서 가장 작은수와 그 다음 작은수를 하는 방법을 사용해야 했다.

# heapq는 일반적인 리스트와 다르게, 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬해준다고 한다.
# 그리고 IndexError를 통해서 -1을 리턴하는 방법도 있었다.

# 다른 사람 풀이 (출처: https://itholic.github.io/kata-more-spicy/)
def solution(scoville, k):
    import heapq

    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt