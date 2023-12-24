def list_operation(command):
    global List
    if command[0:6] == 'insert':
        num = list(filter(lambda x: x.isdigit(), command.split()))
        index = int(num[0])
        value = int(num[1])
        List.insert(index,value)
    elif command[0:6] == 'append':
        value = int(filter(lambda x: x.isdigit(), command.split()))
        List.append(value)
    elif command[0:6] == 'remove':
        value = int(filter(lambda x: x.isdigit(), command.split()))
        List.remove(value)
if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range (0,N):
        command = input()
        command_list = ["append","insert","remove"]
        if command[0:6] in command_list:
            list_operation(command)
        elif command == 'print':
            print(List)
        elif command == 'sort':
            List.sort()
        elif command == 'pop':
            List.pop()
        elif command == 'reverse':
            List.reverse()