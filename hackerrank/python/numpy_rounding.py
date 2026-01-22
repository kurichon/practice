import numpy
numpy.set_printoptions(legacy='1.13')
input_array = list(map(float,input().split()))
print(numpy.floor(input_array))
print(numpy.ceil(input_array))
print(numpy.rint(input_array))
