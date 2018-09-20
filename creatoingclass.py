a=(['+',0],[3,4,1,2,5,1])
b=(['+',3,1],[7,5,1])
def prin(x):
 X,xstr=x[0]+['.']+x[1],''
 for i in range(len(X)):
   xstr+=str(X[i])
 return print(xstr)
prin(a)

if len(a[0][1:])>len(b[0][1:]):
 for i1 in range(len(a[0][1:])-len(b[0][1:])):b[0].insert(1,0)
else:
 for i2 in range(-len(a[0][1:])+len(b[0][1:])):a[0].insert(1,0)

if len(a[1])>len(b[1]):
 for i1 in range(len(a[1])-len(b[1])):b[1].append(0)
else:
 for i2 in range(-len(a[1])+len(b[1])):a[1].append(0)


print(a)
print(b)
