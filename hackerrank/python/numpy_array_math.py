import numpy

N,M = map(int, input().split())

array_A = []
array_B = []

for _ in range (N):
    array_A.append(list(map(int,input().split())))
    
for _ in range (N):
    array_B.append(list(map(int,input().split())))
    
print(numpy.add(array_A,array_B))
print(numpy.subtract(array_A,array_B))
print(numpy.multiply(array_A,array_B))
print(numpy.floor_divide(array_A,array_B))
print(numpy.mod(array_A,array_B))
print(numpy.power(array_A,array_B))
