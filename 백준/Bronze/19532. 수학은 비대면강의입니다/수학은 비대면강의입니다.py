a,b,c,d,e,f = map(int, input().split())

solution = False

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            solution = True
            break
    if solution:
        break
        
        
print(x,y)