n=int(input())
arr=list(map(int, input().split()))
stack=[]
NGE=[-1]*n

for i in range(n):
    x=arr[i]
    while stack and arr[stack[-1]] < x:
        index = stack.pop()
        NGE[index] = x
        
    stack.append(i)
    
for x in NGE:
    print(x, end=' ')
print()