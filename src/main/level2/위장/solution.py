from collections import Counter


def solution(clothes):
    answer = 1
    category = []

    for _, c in clothes:
        category.append(c)

    category_counter = Counter(category)

    for k in category_counter.values():
        answer *= (k + 1)

    return answer - 1

# 계산방법
# (옷의 종류 개수 + 1) 를 곱셈한다, +1을 해주는 이유는 특정 부위의 옷을 입지 않을 수 있기 때문이다.
# 모두 안입는 경우는 없으니 -1 을 해준다.
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# 위 예제의 경우 headgear 2종류, eyewear 1종류이니 3 * 2 - 1 = 5 라서 답이 5가 나온다.

# collections.Counter를 사용하지 않은 솔루션
def other_solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

def otehr_solution2(clothes):
    answer = 1
    dic = dict()
    
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    
    for val in dic.values():
        answer *= (val + 1)
    
    return answer - 1