from copy import deepcopy
ap=(['+',1,0],[1,5,1,2,5,4])
bp=(['+',3,1],[7,5,1,3,4,7])
#Definiendo la función de impresión
def prin(x):
 X,xstr=x[0]+['.']+x[1],''
 for i in range(len(X)):
   xstr+=str(X[i])
 return print(xstr)
a,b=deepcopy(ap),deepcopy(bp)
#Agregando ceros a izquierda y derecha
if len(a[0][1:])>len(b[0][1:]):
 for i1 in range(len(a[0][1:])-len(b[0][1:])):b[0].insert(1,0)
else:
 for i2 in range(-len(a[0][1:])+len(b[0][1:])):a[0].insert(1,0)

if len(a[1])>len(b[1]):
 for i1 in range(len(a[1])-len(b[1])):b[1].append(0)
else:
 for i2 in range(-len(a[1])+len(b[1])):a[1].append(0)
#Suma
s,c=([],[]),1
for k in [1,0]:
  if k==0: c1=0
  else: c1=-1
  for k1 in range(len(a[k])-1,c1,-1):
 #   s[k].append(a[k][k1]+b[k][k1])
   if a[k][k1]+b[k][k1]<10:s[k].append(a[k][k1]+b[k][k1])
   else:a[k][k1-1]+=1;s[k].append(a[k][k1]+b[k][k1]-10)
   #print(a[k][k1],b[k][k1],k,k1)
s[0].reverse();s[1].reverse()

print(s)
#print(a)
#print(b)
