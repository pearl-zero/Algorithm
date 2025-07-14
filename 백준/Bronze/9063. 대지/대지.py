N = int(input())

x = []
y = []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

X=max(x) - min(x)
Y=max(y) - min(y)
print(X*Y)