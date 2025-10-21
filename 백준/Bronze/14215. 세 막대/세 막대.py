a,b,c=map(int, input().split())
stick = sorted([a,b,c])

if stick[0] + stick[1] > stick[2]:
    print(sum(stick))
else :
    print(stick[0]+stick[1]+stick[0]+stick[1]-1)