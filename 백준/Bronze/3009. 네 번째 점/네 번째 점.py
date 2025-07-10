x, y = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x == x1:
    x3 = x2
elif x == x2:
    x3 = x1
else:
    x3 = x
    
if y == y1:
    y3 = y2
elif y == y2:
    y3 = y1
else:
    y3 = y

print(x3, y3)