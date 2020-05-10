import itertools

def is_prime_number(number):
    # 소수란 1보다 크고 1과 자기자신으로만 나누어지는 수
    if number < 2:
        return False
    else:
        for f in range(2, number):
            if number % f == 0:
                return False
    
    return True

def solution(numbers):
    answer = 0
    
    number_list = list(numbers)
    permutation_list = []

    for i in range(1, len(number_list) + 1):
        permutation_list += list(map(''.join, itertools.permutations(number_list, i)))

    # 중복제거는 list(set(ex_list)) 인데, 011과 11이 같은것으로 하기 위해서 int 로 변환 map을 사용
    permutation_list = list(set(map(int, permutation_list)))

    for i in permutation_list:
        if is_prime_number(int(i)):
            answer +=1

    return answer