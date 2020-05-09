import itertools

# itertools.permutation를 사용해서 순열
pool = ['0', '1', '1']
num_list = []
for i in range(1, len(pool) + 1):
  num_list += list(map(''.join, itertools.permutations(pool, i)))

overlap_num_list = list(set(num_list))
print(overlap_num_list)

# 배열에서 중복 제거
ex_list = [1, 1, 2, 3, 3]
overlap_ex_list = list(set(ex_list))
print(overlap_ex_list)

# 배열에서 가장 작은 수, 가장 큰 수 찾기
ex_list = [1, 1, 2, 3, 4, 5, 5]
print(min(ex_list))
print(max(ex_list))

cd = [1, 2, 3, 3, 3, 4, 5, 6, 7]
cd.remove(min(cd))
print(cd)
cd.remove(max(cd))
print(cd)