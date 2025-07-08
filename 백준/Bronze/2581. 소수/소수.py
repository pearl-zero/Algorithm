M = int(input())
N = int(input())

primes = []
for x in range(M,N+1):
    if x > 1 and all(x%i != 0 for i in range(2,x)):
        primes.append(x)

if primes:
    print(sum(primes)) 
    print(min(primes))
else:
    print(-1)