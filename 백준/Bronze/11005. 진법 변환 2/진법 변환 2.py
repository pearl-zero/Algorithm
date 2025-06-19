N, B = map(int, input().split())
result = ""
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N > 0:
    result = digits[N%B] + result
    N //= B

print(result)