n = int(input())
nums = list(map(int, input().split()))

primes = []
for x in nums:
    if x > 1 and all(x % i != 0 for i in range(2, x)):
        primes.append(x)

print(len(primes))