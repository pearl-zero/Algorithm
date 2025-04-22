n = input()
al = 'abcdefghijklmnopqrstuvwxyz'

for i in al:
    if i in n:
        print(n.index(i), end=' ')
    else:
        print(-1, end=' ')