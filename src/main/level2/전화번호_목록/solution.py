# 내가 제출한 코드
def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if phone_book[i] != phone_book[j]:
                if phone_book[i].startswith(phone_book[j]):
                    return False

    return True

"""
문제에 접두어부분은 python startswith endswith가 생각나서 풀은 것 같다.
근데 내 방법이 뭔가 지저분한 거 같아서 다른 사람의 풀이를 찾아보았다.
"""

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

"""
zip과  sorted, [1:]을 이용한 방법인데 훨씬 깔끔해보였다.
sorted에 대한 이해를 돕기 위한 코드
"""

# v = ["119", "97674223", "11", "822", "1195524421"]
# 문제에서 보여준 sorted 결과는 아래처럼 된다.
# ['11', '119', '1195524421', '822', '97674223']

# zip을 이해하기 위해서는 아래 결과를 보면 이해가 훨씬 쉽다.

# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']

"""
for x,y in zip (a,b):
    print(x,y)
"""

# 출력
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e

# 또 다른 사람의 풀이에서 sorted(key = ) 를 이용한 방법도 있었다.

from itertools import combinations as c
def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer