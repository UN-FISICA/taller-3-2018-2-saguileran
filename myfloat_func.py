from copy import deepcopy
import numpy as np
bstr='+120.612379'#str(input('Ingrese el número b con signo: '))
astr='-33.0897'#  str(input('Ingrese el número a con signo: '))
unidad=(['+',1],[0])
munidad=(['-',1],[0])
#Número entero versión tupla
def enterot(n):
    return((['+',n],[0]))
#Llenandon casillas
def filld(x,n):
    for i in range(n): x[1].append(0)
def filli(x,n):
    for i in range(n): x[0].insert(1,0)
#convertiendo una lista a una tupla
def convert(x,d): 
 if d<len(x):
  for u in range(len(x)): x[u]=str(x[u])
  return (list('+'+str(''.join(x[:len(x)-d]))),list(str(''.join(x[len(x)-d:]))))  
 else:print('de es muy grande')  
#Convirtiendo tupla a lista
def convtl(a):
    return(a[0][1:]+a[1])
#Convirtiendo elementos de lista en enteros
def elements(a):
    for i in range(len(a)):a[i]=int(str(a[i]))
def enteros(x):
    for i in range(1,-1,-1):
        for j in range(len(x[i])-1,-1,-1):
            if j==0 and i==0:pass
            else: x[i][j]=int(x[i][j])
#Mismo número de elementos
def compl(a,b):
    if len(a[0])>len(b[0]):filli(b,len(a[0])-len(b[0]))
    if len(a[0])<len(b[0]):filli(a,-len(a[0])+len(b[0]))
    if len(a[1])<len(b[1]):filld(a,-len(a[1])+len(b[1]))
    if len(a[1])>len(b[1]):filld(b,len(a[1])-len(b[1]))
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
#Convierte nparray en tupla
def convlt(x,d,s):
    if s==1:return((['+']+x[:len(x)-d],x[len(x)-d:]))
    if s==0:return((['-']+x[:len(x)-d],x[len(x)-d:]))
AA,BB=convnp(A),convnp(B) # Son tuplas pero con numpy
#Convirtiendo list to str
def convls(a):
    s=''
    for ii in range(len(a)): s+=str(a[ii])
    return(s)
#Tupla más grande
def mayor(a,b):
    compl(a,b)
    A,B=convnp(a),convnp(b)
    if np.array_equal(a,b)==True: return('Son el mismo número')
    else:
        if a[0][0]==b[0][0]:
            np.greater(A[0],B[0])
            i,j=0,0
            while A[i][j]==B[i][j]:
                if len(A[i])-1==j: 
                    i+=1
                    j=0
                else: j+=1
            if A[i][j]>B[i][j] and a[0][0]=='+':return(a)
            elif A[i][j]<B[i][j] and a[0][0]=='+':return(b)
            elif A[i][j]>B[i][j] and a[0][0]=='-':return(b)
            elif A[i][j]<B[i][j] and a[0][0]=='-':return(a)
        else: #signos opuestos
            if '+' in a[0]: return(a)
            else: return(b)
            #elif np.array_equal(a[1],b[1])==False and np.greater(a,b)[1]==True: return(a)
#Corriendo de decenas en tuplas, ingresa una tupla sin el signo con np
def corr(x,neg):
    s=(convnp(x)[0],convnp(x)[1])
    for i in range(1,-1,-1):
        for j in range(len(s[i])-1,-1,-1):
            m=s[i][j]//10
            if i==1 and j==0 and s[i][j]>9: 
                s[0][len(s[0])-1]+=m
                s[i][j]-=10*m
            if s[i][j]>9 and j!=0: 
                s[i][j-1]+=m 
                s[i][j]-=10*m
            if neg==1: #Para una resta
                if i==1 and j==0 and s[i][j]<0: 
                    s[0][len(s[0])-1]+=m
                    s[i][j]-=10*m
                if s[i][j]<0 and j!=0: 
                    s[i][j-1]+=m 
                    s[i][j]-=10*m
    if j==0 and i==0 and s[i][j]>9: 
        s=(np.insert(s[0],0,m),s[1])
        s[0][1]-=10*m+10*(neg)
    return([x[0][0]]+list(s[0]),list(s[1]))
   



def imprimir(x):
    s=''
    for i in range(len(x[0]+['.']+x[1])): s+=str((x[0]+['.']+x[1])[i])
    return(s)


def suma(x, y):
    a,b=deepcopy(x),deepcopy(y)
    #if a[0][0]==b[0][0]:
    compl(a,b)
    s=([a[0][0]]+list(convnp(a)[0]+convnp(b)[0]),list(convnp(a)[1]+convnp(b)[1]))
    return(corr(s,0))

def resta(x, y):
   a,b=deepcopy(x),deepcopy(y)
   compl(a,b)
   pos,neg='+','-'
   A,B=convnp(a),convnp(b)
   a[0][0],b[0][0]='+','+'
   if '-' in x[0]:c1,c=1,0
   else:c,c1=1,0
   if mayor(a,b)==a: #defino a-b, y el resultado va con el signo de a
       s=([pos*c+neg*c1]+list(A[0]+B[0]*-1),list(A[1]+B[1]*-1))
   else: #defino b-a, y el resultado va con el signo de a
       s=([pos*c1+neg*c]+list(A[0]*-1+B[0]),list(A[1]*-1+B[1]))
   return(corr(s,1)) #s es una tupla


def multiplicacion(x, y):
    a,b=deepcopy(x),deepcopy(y)
    A,B=convnp(a),convnp(b)
    da,db,A,B=len(A[1]),len(B[1]),np.concatenate([A[0],A[1]]),np.concatenate([B[0],B[1]])
    m=[]
    for i in range(len(A)-1,-1,-1): #Dejo fijo los componentes de a
        m.append(np.concatenate([A[i]*B,[0]*(len(A)-1-i)]))
    for j in range(len(m)):
        m[j]=corr(convlt(list(m[j]),db,1),0)
    M=m[0]
    for k in range(1,len(m)):
        M=suma(M,m[k])
    M=M[0][1:]+M[1]
    for i1 in range(len(M)):M[i1]=int(M[i1])
    if x[0][0]==y[0][0]:d=1
    else: d=0
    return(convlt(M,db+da,d))

def division(x, y):   #Dividiendo y en x, y/x
    decimales=15
    x,y=deepcopy(y),deepcopy(x)
    sy,sx=y[0][0],x[0][0]
    a=(['+']+x[0][1:],x[1]) #Copia de tupla
    unidad=(['+',1],[])
    filld(unidad,decimales+2)
    compl(unidad,a)
    R,A=[],convtl(a)
    if np.array_equal(a,unidad)==True: return(unidad)
    elif mayor(a,unidad)==a: #a mayor a 1
        Unidad,R=convtl(unidad),[0]
    else: Unidad=convtl(unidad)  #a menor a 1
    while len(Unidad)<len(A):
        R.append(0);Unidad.append(0)
    if int(convls(Unidad))//int(convls(A))==0: Unidad.append(0)
    for iii in range(decimales):
        R.append(int(convls(Unidad))//int(convls(A)))
        Unidad=list(str(int(convls(Unidad))%int(convls(A))))
        elements(Unidad)
        if int(convls(Unidad))<int(convls(A)):Unidad.append(0)
    R=5*[0]+R
    if float(astr)<1:
        decimales+=1
        Div=convert(R,decimales-1)#para A<0
    if float(astr)>1:Div=convert(R,decimales)  #para A>0
    
    #return(R,decimales,len(R))
    Div=([sx]+Div[0][1:],Div[1])
    enteros(Div)
    return(multiplicacion(Div,y))

def comparacion(a, b):
    if np.array_equal(a,b)==True: return('Son el mismo número')
    else:print('Números diferentes')


def pi(n):
    k,R= (['+',1],[0]),[]#Primer término
    for i in range(n):
        if i%2==0:f=unidad
        else: f=munidad
        denominador=suma(multiplicacion(enterot(i),enterot(2)),unidad)
        numerador=f
        R.append(division(numerador,denominador))
    M=enterot(0)
    for j in range(len(R)):
        M=suma(M,R[j])
    return(multiplicacion(enterot(4),M))
print(pi(4))
#if __name__    == "__main__":
#    print(imprimir(pi()))
