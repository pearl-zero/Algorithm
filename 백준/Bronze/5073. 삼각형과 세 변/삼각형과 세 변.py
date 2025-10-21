while True:
    try:
        a,b,c = map(int, input().split())
        
        if a==b==c==0:
            break
            
        sides = sorted([a,b,c])
        if sides[2] >= sides[0] + sides[1]:
            print("Invalid")
            continue
            
        if a==b==c:
            print("Equilateral")
        elif a==b or b==c or c==a:
            print("Isosceles")
        else:
            print("Scalene")

    except (ValueError, IndexError):
        print("Invalid")