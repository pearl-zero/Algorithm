import math

A,B,V = map(int, input().split())

days = math.ceil((V-A)/(A-B)) 
print(days+1)