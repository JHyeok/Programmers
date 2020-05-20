# 10진수를 2진수로
def change_binary(n: int) -> int:
    result, idx = 0, 0
    
    while (n >= 1):
        remainder = n % 2

        # '/'는 나눗셈을 의미하며 결과가 float로 나옴
        # '//'는 나눗셈을 의미하며 결과가 int로 나옴
        n = n // 2

        # **는 거듭제곱, *는 곱
        result += (10 ** idx) * remainder
        idx += 1
    
    return result

# 2진수를 10진수로
def binary_to_decimal(binary_num):
    decimal_number = 0

    # 2진수 숫자를 문자열 string으로 변환
    binary_num_str = str(binary_num)

    # 2진수 문자열의 각 자릿값에 2의 n 제곱 형태로 가중치를 계산하여 합산
    # pow 함수는 pow(2, 3)은 2의 3승 = 8 이다.
    for i, digit in enumerate(binary_num_str):
        decimal_number += int(digit) * pow(2, len(binary_num_str) - 1 -i)
    
    return decimal_number

# 거품 정렬
# 단순하지만 O(N^2)의 상대적으로 느린 시간 복잡도
# 인접한 두 원소를 비교하여(이중 for문 사용) 스왑하는 것을 반복하여 정렬한다
def bubble_sort(x):
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j] #swap
    
    return x

# 퀵 정렬
# 메모리 사용량도 적고 구현하기도 용이
# 전체에서 기준(pivot)이 되는 원소를 하나 정하고 이 기준을 중심으로
# 기준 왼쪽으로는 기준보다 작은 값이 오게 정렬, 기준 오른쪽으로는 큰 값이 오게 정렬
# 위 과정을 반복
# 일반적으로 O(NlogN)의 시간 복잡도이지만, pivot 선택을 최악으로 하면 O(N^2)의 시간복잡도
def quick_sort(x):
    if len(x) <= 1:
        return x
    
    pivot = x[len(x) // 2]
    left, right, equal = [], [], []

    for a in x:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    return quick_sort(left) + equal + quick_sort(right)

# 삽입 정렬
# 배열의 각각의 원소들을 앞에서부터 차례대로 이미 정렬된 부분 배열과 비교하여
# 자신보다 큰 값과 작은 값 사이에 적당한 위치를 찾아 삽입하여 정렬
# 시간복잡도는 O(N^2)
def insertion_sort(x):
    for i in range(1, len(x)):
        for j in range(i, 0, -1):
            if x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
    return x

ex_list = [100, 110, 3, 55, 23, 77, 1, 39, 43, 67, 8, 20]
print(bubble_sort(ex_list))
print(quick_sort(ex_list))
print(insertion_sort(ex_list))


# 참고
# https://blog.doosikbae.com/117
# https://blog.naver.com/PostView.nhn?blogId=okkam76&logNo=221365923066&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=false&from=postView
# https://potensj.tistory.com/33