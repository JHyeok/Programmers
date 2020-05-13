def solution(progresses, speeds):
    answer = []
    works = [0] * len(progresses)
    position = 0    

    # 각 기능마다 몇 일 걸리는지 계산
    # 예제 기준으로 [7, 3, 9]
    for p, s in zip(progresses, speeds):
        while True:
            if p < 100:
                works[position] += 1
                p += s
            else:
                position += 1
                break

    # 몇 일째에 몇개의 기능이 배포되는지 계산
    # [7, 3, 9] 에서 7,3 은 7일째에 2개, 9는 9일째에 1개 배포 return [2, 1]
    cnt = 0
    first_works = works[0]
    for i in works:
        if first_works >= i:
            cnt += 1 
        else:
            answer.append(cnt)
            first_works = i
            cnt = 1
    
    answer.append(cnt)

    return answer