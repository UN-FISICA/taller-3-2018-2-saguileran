from copy import deepcopy
import math
import numpy as np
astr='+7423.1239'#str(input('Ingrese el número b con signo: '))
bstr='+0.789700999139'#  str(input('Ingrese el número a con signo: '))
#Definiendo print de una tupla
def prin(x):
    s=''
    for i in range(len(x[0]+['.']+x[1])): s+=str((x[0]+['.']+x[1])[i])
    return(s)
#Convierte strings en tuplas con elementos enteros
def conven(s):
    s=(list(s[:s.find('.')]),list(s[s.find('.')+1:]))
    for i in range(2):
        for j in range(len(s[i])):
            if s[i][j]=='+' or s[i][j]=='-': pass
            else: s[i][j]=int(s[i][j])        
    return(s)
A,B=conven(astr),conven(bstr) #A,B son tuplas!
#Parte decima y parte entera, tupla
def convnp(a):
    return(np.asarray(a[0][1:]),np.asarray(a[1]))
AA,BB=convnp(A),convnp(B)
#Llenandon casillas
def filld(x,n):
    for i in range(n): x[1].append(0)
def filli(x,n):
    for i in range(n): x[0].insert(1,0)
#Suma entre tuplas, ingreso tuplas, asummiendo que tienen el mismo signo
def suma(a,b):
    if a[0][0]==b[0][0]:
        if len(a[0])>len(b[0]):filli(b,len(a[0])-len(b[0]))
        if len(a[0])<len(b[0]):filli(a,-len(a[0])+len(b[0]))
        if len(a[1])<len(b[1]):filld(a,-len(a[1])+len(b[1]))
        if len(a[1])>len(b[1]):filld(b,len(a[1])-len(b[1]))
        s=(convnp(a)[0]+convnp(b)[0],convnp(a)[1]+convnp(b)[1]) #Tupla suma con 2 dígitos
        for i in range(1,-1,-1):
            for j in range(len(s[i])-1,-1,-1):
                if i==1 and j==0 and s[i][j]>9: 
                    s[0][len(s[0])-1]+=1
                    s[i][j]-=10
                if s[i][j]>9 and j!=0: 
                    s[i][j-1]+=1 
                    s[i][j]-=10
        if j==0 and i==0 and s[i][j]>10: 
            s=(np.insert(s[0],0,1),s[1])
            s[i][1+j]-=10
        return(([a[0][0]]+list(s[0]),list(s[1])))
    else: print('Signos diferentes')
#Al hacer uso de esta función las tuplas quedan con la misma cantidad de elementos
#Tupla mayor
def great(x,y):
    if a[0][0]==b[0][0]:
        u,i,j=suma(x+y),0,0
        while np.greater(x[0][],y[0][]):
    else:
        if x[0][0]=='+':return(x)
        else: return(y)
#Resta
 
print(suma(A,B))
#print(A)
#print(B)