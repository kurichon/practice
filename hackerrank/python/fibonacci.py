cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = []
    for i in range(n):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-2]+fib_list[-1])
    return fib_list
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
