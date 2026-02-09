numbers = []
for i in range(5):
    numbers.append(int(input()))

sums = sum(numbers)


ave = sums//5
print(ave)

numbers.sort()
print(numbers[2])