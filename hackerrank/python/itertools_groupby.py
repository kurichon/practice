import itertools
groups = []
S = input()
for k, g in itertools.groupby(S):
    groups.append((len(list(g)),int(k)))      # Store group iterator as a list


print(*groups)
