# -*- coding: utf-8 -*-
#MÃ¡xima cantidad de elementos en una lista
#import sys
#print('MÃ¡xima cantidad de elementos de una lista '+str(sys.maxsize))
from copy import deepcopy
#import numpy as np
bstr='12320.1239'#str(input('Ingrese el número b con signo: '))
astr='+0.321'#  str(input('Ingrese el número a con signo: '))
if ('+' or '-') not in bstr:bstr='+'+bstr
if ('+' or '-') not in bstr:astr='+'+astr
#Convirtiendo list to str
def convls(a):
    s=''
    for ii in range(len(a)): s+=str(a[ii])
    return(s)
#COnvirtiendo tupla a str
def convtl(a):
    return(a[0][1:]+a[1])
#Convirtiendo string a número 
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
 else: pass#print('Número de decimals más grande que numero de digitos')
#COnvirtiendo elementos de lista en enteros
def elements(a):
    for i in range(len(a)):a[i]=int(str(a[i]))
#Definiendo la función de impresión
def prin(x):
 X,xstr=x[0]+['.']+x[1],''
 for i in range(len(X)):
   xstr+=str(X[i])
 return print(xstr)
a,b=deepcopy(ap),deepcopy(bp)
#Definiendo la función comparación
def comp(a,b):
    if len(a[1])==len(b[1]) and len(a[0])==len(b[0]): 
        for i in range(len(a)):
            for i1 in range(len(a[i])):
                if a[i][i1]==b[i][i1]: 
                    return(print('Son la misma cantidad'))
            else: 
                return(print('NO son la misma cantidad, son diferentes números'))
                break
    else: return(print('NO son la misma cantidad, son diferentes números'))
#Tupla mayor
def mayt(p,v):
    if len(p[0][1:])>len(v[0][1:]):return(p)
    elif len(p[0][1:])<len(v[0][1:]):return(v)
    elif len(p[0][1:])==len(v[0][1:]): 
        c=0
        for i in range(1,len(p[0][1:])):
            if int(p[0][i])>int(v[0][i]):return(p); c=1; break 
            if int(p[0][i])<int(v[0][i]):return(v); c=1; break
        if c==0:
            for j in range(max(len(p[1]),len(v[1]))):
                if int(p[1][j])>int(v[1][j]):print((p[1][j],(v[1][j]))); return(p); break 
                else: return(v); break 
#Agregando ceros a izquierda y deint(convls(Unidad))%int(convls(A))recha
def filld(a,n):
    for i11 in range(n):a[1].append(0)
def filli(a,n):
    for i11 in range(n):a[0].insert(1,0)
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
#Suma, ingresan listas
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
def mult(astr,bstr):
 A=list(astr[1:astr.find('.')]+astr[astr.find('.')+1:])
 B=list(bstr[1:bstr.find('.')]+bstr[bstr.find('.')+1:])
 #print(A)#print(B)
 M,m,c,ct=[],[],0,0
 for d in range(len(A)-1,-1,-1):
  for d1 in range(len(B)-1,-1,-1):
   if int(A[d])*int(B[d1])+c<10: m.insert(0,int(A[d])*int(B[d1])+c);c=0
   else: 
    m.insert(0,int(str(int(A[d])*int(B[d1])+c)[1]))
    c=int(str(int(A[d])*int(B[d1])+c)[0])
   if d1==0 and c!=0:m.insert(0,c); c=0
  M.append(m+ct*['0'])
  m,ct=[],ct+1
 for d2 in range(len(M)):
  m.insert(0,convert(M[d2],len(conv(bstr)[1])))
 D=m[0]
 for d3 in range(1,len(m)):
  D=sum1(D,m[d3])
 d11=convert(D[0][1:]+D[1],len(a[1])+len(b[1]))
 return(prin(d11))
mult(astr,bstr)

#definiendo la división 1/A
decimales=10#int(input('Ingrese el número de decimales '))
unidad=(['+',1],[])
filld(unidad,len(a[1]))
R,A=[],convtl(a)
if mayt(a,unidad)==a: #a mayor a 1
    Unidad,R=convtl(unidad),[0,'.']
    while len(Unidad)<len(A):
        R.append(0);Unidad.append(0)
    Unidad.append(0)
    for iii in range(decimales):
        R.append(int(convls(Unidad))//int(convls(A)))
        Unidad=list(str(int(convls(Unidad))%int(convls(A))))
        elements(Unidad)
        if int(convls(Unidad))<int(convls(A)):Unidad.append(0)
    Div=([R[0]],R[2:])
else:  #a menor a 1
    Unidad,R=convtl(unidad),[0,'.']
    

#if float(convls(A))>float(convls(unidad)):
#    while float(convls(A))>=float(convls(unidad)):
 #       unidad.append(0)
  #      R.append('0')
   # R.append(1)
    #print(float(convls(unidad))-float(convls(A)))
    
   
            
#A=list(astr[1:astr.find('.')]+astr[astr.find('.')+1:])
#B=list(bstr[1:bstr.find('.')]+bstr[bstr.find('.')+1:])
#if len(b[1])>len(a[1]): 
    
    
    
    
    