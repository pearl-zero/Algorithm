n = int(input())
stack = []

for _ in range(n):
    command = input().strip().split()  # 그냥 split() 사용
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)
