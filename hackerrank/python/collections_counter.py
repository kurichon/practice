# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = input()
shoes = Counter(map(int, input().split()))
N = int(input())

purchase_sum = []

for _ in range(N):
    shoe_size, shoe_price = map(int, input().split())
    if (shoes[shoe_size] > 0):
        purchase_sum.append(shoe_price)
        shoes[shoe_size] -= 1
        #remove shoe from list
    else:
        continue #shoe not available no sale
print(sum(purchase_sum))
