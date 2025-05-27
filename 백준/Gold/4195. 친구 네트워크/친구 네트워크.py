def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])  # 경로 압축
        return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parent[y_root] = x_root
        number[x_root] += number[y_root]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
