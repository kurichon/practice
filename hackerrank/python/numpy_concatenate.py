import numpy

N,M,P = map(int,(input().split()))
array_N = []
array_M = []

for i in range(N):
    array_N.append(list(map(int,input().split())))
for _ in range(M):
    array_M.append(list(map(int,input().split())))
        
array_np = numpy.concatenate((array_N,array_M))
print(array_np)
