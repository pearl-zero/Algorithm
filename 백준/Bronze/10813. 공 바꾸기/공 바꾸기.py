n, m = map(int, input().split())
basket = [0] * n

# 바구니에 1~n까지 번호 넣기
for i in range(n):
    basket[i] = i + 1

# m번 동안 공을 교환
for _ in range(m):
    a, b = map(int, input().split())
    c = basket[a - 1]
    basket[a - 1] = basket[b - 1]
    basket[b - 1] = c

# 최종 상태 출력
for i in range(n):
    print(basket[i], end=' ')
