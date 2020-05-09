def solution(n, lost, reserve):
    answer = n - len(lost)

    # n : 전체학생수
    # lost : 잃어버린 사람
    # reserver : 두개를 가져온 사람
    # 여벌 체육복을 가져온 사람이 잃어버린 경우
    for i in range(0, len(lost)):
        for j in range(0, len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1
                answer += 1
                break

    # 체육복을 빌려주면 -1을 넣는다. 빌려주는지 여부는 -를 해서 절댓값이 1인지 확인하면 된다.
    for i in range(0, len(lost)):
        for j in range(0, len(reserve)):
            if abs(lost[i] - reserve[j]) == 1:
                reserve[j] = -1
                answer += 1
                break

    return answer

# 다른 사람의 풀이
def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        for x in range(l-1, l+2):
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved