import sys
input = sys.stdin.readline

a = int(input())

a = list(str(a))
a.sort(reverse=True)

print(''.join(a))   