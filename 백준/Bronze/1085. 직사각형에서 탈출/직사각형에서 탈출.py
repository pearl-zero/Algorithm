x,y,w,h = map(int, input().split())

langth = [x, y, w-x, h-y]
result = min(langth)
print(result)    