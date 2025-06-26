n = int(input())

layer = 1
max_num = 1

while n > max_num :
    layer += 1
    max_num += layer
    
a = max_num - n

if layer % 2 == 0 :
    b = layer - a
    c = 1 + a        
else:
    b = 1 + a
    c = layer - a
    
print(f"{b}/{c}")