from itertools import permutations
input_var = input().split(' ')
S = str(input_var[0])
k = int(input_var[1])
assert 0 < k < len(S)
perms = sorted(list(permutations(S,k)))
for p in perms:
    print(''.join(p))
