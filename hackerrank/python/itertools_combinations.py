from itertools import combinations

S, k = input().split()
k = int(k)

assert 0 < k <= len(S)

def print_combos(S, r):
    for c in combinations(sorted(S), r):
        print(''.join(c))
for i in range(1, k+1):
    print_combos(S,i)
