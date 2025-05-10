def handle_command(command,arr):
    match command[0]:
        case 'insert':
            arr.insert(int(command[1]),int(command[2]))
        case 'print':
            print(arr)
        case 'remove':
            arr.remove(int(command[1]))
        case 'append':
            arr.append(int(command[1]))
        case 'sort':
            arr.sort()
        case 'pop':
            arr.pop()
        case 'reverse':
            arr.reverse()

if __name__ == '__main__':
    N = int(input())
    arr = [] #init list
    for _ in range (N):
        input_str = input()
        command = input_str.split(' ')
        handle_command(command,arr)
