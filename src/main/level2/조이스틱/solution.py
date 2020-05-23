# left, right를 구하는 부분은 다른 답지를 참고
def solution(name):
    answer = 0
    where = 0
    min_up_down = []
    alphabet_front = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    alphabet_back = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet_back = alphabet_back[::-1]

    # min_up_down을 구한다
    # 알파벳을 움직여서 맞추는 최소 횟수를 저장하는 배열이다.
    for idx, alphabet in enumerate(name):
        if alphabet != "A":
            if alphabet in alphabet_back:
                min_up_down.append(alphabet_back.index(alphabet) + 1) 
            elif alphabet in alphabet_front:
                min_up_down.append(alphabet_front.index(alphabet))
        else:
            min_up_down.append(0)

    while True:
        answer += min_up_down[where]
        min_up_down[where] = 0

        # 탈출 조건
        if sum(min_up_down) == 0:
            break

        left, right = (1, 1)

        # min_up_down[where - left]의 값이 0 보다 작으면 계속해서 증가
        while min_up_down[where - left] <= 0:
            left += 1
        
        # min_up_down[where + right]의 값이 0 보다 작으면 계속해서 증가
        while min_up_down[where + right] <= 0:
            right += 1

        # left와 right를 비교해서 더 작은 수를 더한다
        if left < right :
            answer += left
            where -= left
        else :
            answer += right
            where += right

    return answer

# 다른 사람의 풀이
def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]       

    answer = 0
    where = 0

    while True:    
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer