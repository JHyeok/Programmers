def solution(brown, yellow):
    answer = []
    possible_num = []
    area = brown + yellow

    for i in range(1, area + 1):
        if area%i == 0:
            possible_num.append(i)

    for i in possible_num:
        # if i>2 and i*2 + (area/i) * 2 - 4 == brown:
        if (i + area/i) * 2 - 4 == brown:
            answer.append(i)

    if len(answer) == 1:
        answer.append(answer[0])

    answer.sort(reverse=True)

    return answer

param1 = 8
param2 = 1
print(solution(param1, param2)) # return [4, 3]

# 노랑카펫 1
# 브라운카펫 8
# 길이(가로, 세로) 3, 3

# 노랑카펫 2
# 브라운카펫 10
# 길이(가로, 세로) 4, 3

# 노랑카펫 24
# 브라운카펫 24
# 길이(가로, 세로) 8, 6

# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6] 

# brown과 yellow의 길이가 제한되어 있다.
# 가로길이 weight
# 세로길이 height
# weight >= height
# 브라운과 엘로우의 숫자를 더하면 return 하는 값의 너비가 된다.

# brown + yellow = total
# total

# 풀이
# 곱셈으로 total 이 나올 수 있는 경우의 수를 구한다. 약수를 구한다.
# brown의 개수는 (가로+세로) * 2 - 4 이다.
# 약수를 하나씩 꺼내서 위 식이 성립하는지 확인한다.
# 그리고 가로는 세로보다 길이가 같거나 크기 때문에 sort 해준다.
# 그리고 가로 세로가 같은 경우, 예를 들어 테스트 케이스 2의 경우에는
# 넓이는 9이고, 약수는 [1, 3, 9] 이다. 이렇게 가로 세로가 같은 경우에는 약수가 이렇게 나오는데
# 그래서 마지막에 저 공식이 성립해도 answer 배열에 들어가는 길이는 1이다.
# 그렇기 떄문에 길이가 1인경우, 가로 세로가 같은 것이라고 간주하고 배열에 같은 값을 추가해준다.