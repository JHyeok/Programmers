def solution(array, commands):
    answer = [0] * len(commands)

    cnt = 0
    for i, j, k in commands:
        arr1 = array[i-1:j]
        arr1.sort()
        answer[cnt] = arr1[k - 1]
        cnt += 1

    return answer

# 다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 다른 사람의 풀이2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer