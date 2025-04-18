n,m=map(int,input().split())

basket = [0]*n
for i in range(n):
    basket[i] = i+1

for _ in range(m):
    a,b=map(int,input().split())
    c=basket[a-1:b]
    c.reverse()
    basket[a-1:b]=c
    
for i in range(n):
    print(basket[i], end=" ")