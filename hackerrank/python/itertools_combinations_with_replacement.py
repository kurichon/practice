from itertools import combinations_with_replacement
S,k = input().strip().split()
k = int(k)
S = sorted(S)
assert 0< k <= len(S)

result = list(combinations_with_replacement(S,k))

for i in result:
    print(''.join(i))
