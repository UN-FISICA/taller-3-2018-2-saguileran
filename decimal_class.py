#Máxima cantidad de elementos en una lista
#import sys
#print('Máxima cantidad de elementos de una lista '+str(sys.maxsize))
from copy import deepcopy
#import numpy as np
bstr='+123.12355'#str(input('Ingrese el número b con signo: '))
astr='+1234685.123'#  str(input('Ingrese el número a con signo: '))
if ('+' or '-') not in bstr:bstr='+'+bstr
if ('+' or '-') not in bstr:astr='+'+astr
#Convirtiendo string a número 
def conv(x):
 ap=(list((x.split('.'))[0]),list((x[1:].split('.'))[1]))
 for f in [0,1]:
  for f1 in range(len(ap[f])):
    if ap[f][f1]=='+' or ap[f][f1]=='-': pass
    else: ap[f][f1]=int(ap[f][f1])
 return(ap)
ap=conv(astr);bp=conv(bstr)
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
def sum(a,b):
 if a[0][0]==b[0][0]:
  s,c=([],[]),1
  for k in [1,0]:
    if k==0: c1=0
    else: c1=-1
    for k1 in range(len(a[k])-1,c1,-1):
     if a[k][k1]+b[k][k1]<10:s[k].append(a[k][k1]+b[k][k1])
     else:
         s[k].append(a[k][k1]+b[k][k1]-10)
         if k1==0 and k==1:a[0][len(a[0])-1]+=1 
         else:a[k][k1-1]+=1
  s[0].reverse();s[1].reverse();s[0].insert(0,a[0][0])
  return(prin(s))
 else:print('Resta')
#Multiplicación     #Puedo convertirlo a flotante y multiplicar y ya!
A=list(astr[1:astr.find('.')-1]+astr[astr.find('.')+1:])
B=list(bstr[1:bstr.find('.')-1]+bstr[bstr.find('.')+1:])
print(A)
print(B)
#cont,Cont,SUM=0,[],[]
#for d in range(len(A)):
# for d1 in range(len(B)):
#  Cont.append(A[d]*B[d1])
# SUM.appned(Count)
#for d2 in range(len(SUM)):
 
    
#print(astr)
#print(bstr) 