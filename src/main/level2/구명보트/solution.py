# 보트는 사람들을 구출할 수 없는 경우는 없다.
# 그리고 구명보트는 작아서 한 번에 최대 2명
# 무게가 큰 순서대로 정렬
# 제일 무거운 사람의 위치를 first, 가장 가벼운 사람의 위치를 last
# first에 위치한 사람을 내보내고, last에 위치하는 사람의 무게와 합이 limit 이하인지 확인
# 무게의 합이 limit 보다 크면 first만 증가시켜서 내보내고
# 아니라면 first도 내보내고, last도 내보내기 때문에 first의 값은 증가, last의 값은 감소한다
# 모든 인원이 나가는 것은 first >= last 일 때이다.
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    first = 0
    last = len(people) - 1

    while first <= last:
        if people[first] + people[last] > limit:
            first += 1
        else:
            first += 1
            last -= 1
    
    answer = first
    return answer

param1 = [70, 50, 80, 50] # [70, 80, 50]
param2 = 100 # 100

print(solution(param1, param2)) # return 3