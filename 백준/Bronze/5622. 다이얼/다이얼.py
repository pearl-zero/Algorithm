dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alp = list(input())
result = 0
    
for i in alp:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            result += num
print(result)