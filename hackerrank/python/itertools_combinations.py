from itertools import combinations

S,k = input().strip().split()

assert 0 < int(k) <= len(S)
result_1 = sorted(''.join(c) for c in map(sorted, combinations(S, 1)))
result_2 = sorted(''.join(c) for c in map(sorted, combinations(S, int(k))))
for i in result_1:
    print(''.join(i))
for j in result_2:
    print(''.join(j))
