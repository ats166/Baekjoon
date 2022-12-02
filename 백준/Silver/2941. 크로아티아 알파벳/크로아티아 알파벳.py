N = input()

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for cro in croa:
    N = N.replace(cro, 'P')
print (len(N))