from itertools import product

A = input().split()
B = input().split()

pairs = [tuple(map(int, p)) for p in product(A, B)]
for p in pairs:
    print(p,end=" ")
