import sys

a = int(input())

for i in range(a):
    c,b = map(int, sys.stdin.readline().split())
    print(c+b)