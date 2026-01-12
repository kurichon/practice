from itertools import product
def get_max(num_list):
    result_list = []
    for num in num_list:
        result_list.append((int(num) ** 2))
    return result_list
    
K, M = input().split()
K = int(K)
M = int(M)
input_list = []
sum_list = []
elem_count = []
for i in range(K):
    
    input_list = input().split()
    elem_count.append(int(input_list[0]))
    elem_list = input_list[1:]
    sum_list.append(get_max(elem_list))
max_sum = max(sum(combo) % M for combo in product(*sum_list))
print(max_sum)   
    
