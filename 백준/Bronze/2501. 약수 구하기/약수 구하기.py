a, b = map(int, input().split())

nums = []
for num in range(1,a+1):
    if a % num == 0:
        nums.append(num)

if len(nums) >= b:
        print(nums[b-1])      
else:
    print(0) 