#Máxima cantidad de elementos en una lista
#import sys
#print('Máxima cantidad de elementos de una lista '+str(sys.maxsize))
from copy import deepcopy
#import numpy as np
bstr='+7263.393679'#str(input('Ingrese el n�mero b con signo: '))
astr='+18972364.128'#  str(input('Ingrese el n�mero a con signo: '))
if ('+' or '-') not in bstr:bstr='+'+bstr
if ('+' or '-') not in bstr:astr='+'+astr
#Convirtiendo string a n�mero 
def conv(x):
 ap=(list((x.split('.'))[0]),list((x[1:].split('.'))[1]))
 for f in [0,1]:
  for f1 in range(len(ap[f])):
    if ap[f][f1]=='+' or ap[f][f1]=='-': pass
    else: ap[f][f1]=int(ap[f][f1])
 return(ap)
ap=conv(astr);bp=conv(bstr)
#convertiendo una lista a un string
def convert(x,d): 
 if d<len(x):
  for u in range(len(x)): x[u]=str(x[u])
  return (list('+'+str(''.join(x[:len(x)-d]))),list(str(''.join(x[len(x)-d:]))))
 else: pass#print('N�mero de decimals m�s grande que numero de digitos')

#Definiendo la funci�n de impresi�n
def prin(x):
 X,xstr=x[0]+['.']+x[1],''
 for i in range(len(X)):
   xstr+=str(X[i])
 return print(xstr)
a,b=deepcopy(ap),deepcopy(bp)
#Agregando ceros a izquierda y derecha
def fill(a,b):
 if len(a[0][1:])>len(b[0][1:]):
  for i1 in range(len(a[0][1:])-len(b[0][1:])):b[0].insert(1,0)
 else:
  for i2 in range(-len(a[0][1:])+len(b[0][1:])):a[0].insert(1,0)
 if len(a[1])>len(b[1]):
  for i1 in range(len(a[1])-len(b[1])):b[1].append(0)
 else:
  for i2 in range(-len(a[1])+len(b[1])):a[1].append(0)
 return(a,b)
#Suma
def sum1(a,b):
 a,b=fill(a,b)[0],fill(a,b)[1]
 if a[0][0]==b[0][0]:
  s,c,v=([],[]),0,0
  for k in [1,0]:
    if k==0: c1=0
    else: c1=-1
    for k1 in range(len(a[k])-1,c1,-1):
     if int(a[k][k1])+int(b[k][k1])+v<10:s[k].append(int(a[k][k1])+int(b[k][k1])+v);v=0
     else:
         s[k].append(int(a[k][k1])+int(b[k][k1])+v-10)
         v=1
    if v!=0 and k==0 and k1==1: s[0].append(v) 
  s[0].reverse();s[1].reverse();s[0].insert(0,a[0][0])
  return(s)
 else:print('Resta')

#Multiplicación     #Puedo convertirlo a flotante y multiplicar y ya!
A=list(astr[1:astr.find('.')]+astr[astr.find('.')+1:])
B=list(bstr[1:bstr.find('.')]+bstr[bstr.find('.')+1:])
print(A)
print(B)
M,m,c,ct=[],[],0,0
for d in range(len(A)-1,-1,-1):
 for d1 in range(len(B)-1,-1,-1):
  if int(A[d])*int(B[d1])+c<10: m.insert(0,int(A[d])*int(B[d1])+c);c=0
  else: 
   m.insert(0,int(str(int(A[d])*int(B[d1])+c)[1]))
   c=int(str(int(A[d])*int(B[d1])+c)[0])
  if d1==0 and c!=0:m.insert(0,c) 
 M.append(m+ct*['0'])
 m,ct=[],ct+1
for d2 in range(len(M)):
 m.insert(0,convert(M[d2],len(conv(bstr)[1])))
D=m[0]
for d3 in range(1,len(m)):
 D=sum1(D,m[d3])
d11=convert(D[0][1:]+D[1],len(a[1])+len(b[1]))
#print(astr)
#print(bstr) 