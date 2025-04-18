stdnt = []
for _ in range(28):
    s=int(input())
    stdnt.append(s)

n_stdnt = []
for i in range(1, 31):
    if i not in stdnt:
        n_stdnt.append(i)
        
print(min(n_stdnt), max(n_stdnt))
