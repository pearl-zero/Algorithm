a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

if a1 <= c and (a1-c)*n + a2 <= 0:
    print(1)
else:
    print(0)