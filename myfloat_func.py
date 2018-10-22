from copy import deepcopy
import numpy as np
#bstr='+4.0'#str(input('Ingrese el número b con signo: '))
#astr='-1.33333'#  str(input('Ingrese el número a con signo: '))
unidad=(['+',1],[0])
munidad=(['-',1],[0])
#Número entero versión tupla
def enterot(n):
    return(corr((['+',n],[0]),0))
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
            else:
                if x[i][j]!='.':x[i][j]=int(x[i][j])
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
#A,B=conven(astr),conven(bstr) #A,B son tuplas!
#Parte decima y parte entera, tupla array
def convnp(a):
    return(np.asarray(a[0][1:]),np.asarray(a[1]))
#Convierte nparray en tupla
def convlt(x,d,s):
    if s==1:return((['+']+x[:len(x)-d],x[len(x)-d:]))
    if s==0:return((['-']+x[:len(x)-d],x[len(x)-d:]))
#AA,BB=convnp(A),convnp(B) # Son tuplas pero con numpy
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
def corr(s,n):
    x=(convnp(s)[0],convnp(s)[1])
    for i in range(1,-1,-1):
        for j in range(len(x[i])-1,-1,-1):
            m=x[i][j]//10
            if n==0:
                if x[i][j]>9 and not(i==1 and j==0) and not(i==0 and j==0):
                    x[i][j]-=10*m
                    x[i][j-1]+=1*m
                elif x[i][j]>9 and (i==1 and j==0): 
                     x[0][len(x[0])-1]+=1*m
                     x[1][0]-=10*m
                elif x[0][0]>9 and i==0:
                    x[0][0]-=10*m
                    x=(np.insert(x[0],0,m),x[1])
#Modificaciones para negativos
            else:
                if x[i][j]<0 and not(i==1 and j==0) and not(i==0 and j==0):
                    x[i][j]-=10*m
                    x[i][j-1]+=1*m
                elif x[i][j]<0 and (i==1 and j==0): 
                    x[1][0]-=10*m
                    x[0][len(x[0])-1]+=1*m
                elif x[0][0]<0 and i==0 and n==1:
                    x[0][0]-=10*m
    return([s[0][0]]+list(x[0]),list(x[1]))
#ELimiando ceros a izquierda y derecha, tuplas
def rmd(x):
    i=len(x[1])-1
    while (x[1][i]==0) and (len(x[1])>2):
        x[1].pop()
        i-=1
    return(x)
#Eliminando ceros a izquierda
def rmi(x):
    i=1
    while x[0][i]==0 and (len(x[0])>2):x[0].pop(1)
    return(x)

def imprimir(x):
    s=''
    for i in range(len(x[0]+['.']+x[1])): s+=str((x[0]+['.']+x[1])[i])
    return(s)


def suma(x, y):
    a,b=deepcopy(x),deepcopy(y)
    compl(a,b)
    if x[0][0]==y[0][0]:
        s=([x[0][0]]+list(convnp(a)[0]+convnp(b)[0]),list(convnp(a)[1]+convnp(b)[1]))
        return(corr(s,0))
    else: 
       A,B,i=convnp(a),convnp(b),0
       Ac,Bc=list(convnp(a)[0])+list(convnp(a)[1]),list(convnp(b)[0])+list(convnp(b)[1])
       #print(Ac,Bc)
       i=len(Ac)-1
       while Ac[i]>Bc[i]==True:
          i-=1
       #print(Ac,Bc,x[0][0],i)
       if i==len(Ac)-1:
           s=([x[0][0]]+list(A[0]+B[0]*-1),list(A[1]+B[1]*-1))
           #s=([y[0][0]]+list(A[0]*-1+B[0]),list(A[1]*-1+B[1]))
       else: #defino b-a, y el resultado va con el signo de a
           #s=([x[0][0]]+list(A[0]+B[0]*-1),list(A[1]+B[1]*-1))
           s=([y[0][0]]+list(A[0]*-1+B[0]),list(A[1]*-1+B[1]))
       return(corr(s,1)) #s es una tupla

def resta(x, y):
   a,b=deepcopy(x),deepcopy(y)
   compl(a,b)
   if a[0][0]!=b[0][0]:
       if ('+' in b[0])==True:b=(['-']+b[0][1:],b[1])
       else: b=(['+']+b[0][1:],b[1])
       return(corr(suma(a,b),1))
   else: 
       sig=b[0][0]
       if b[0][0]=='+': sigop='-'
       else:sigop='+'
       A,B=convnp(a),convnp(b)
       if np.greater(a,b)[0]==True: #defino a-b, y el resultado va con el signo de a
           s=([sig]+list(A[0]+B[0]*-1),list(A[1]+B[1]*-1))
       else: #defino b-a, y el resultado va con el signo de a
           s=([sigop]+list(A[0]*-1+B[0]),list(A[1]*-1+B[1]))
       return(corr(s,1)) #s es una tupla



def multiplicacion(x, y):
    da,db=len(x[1]),len(y[1])
    a,b,m=deepcopy(x),deepcopy(y),[]
    A,B=convnp(a),convnp(b)
    A,B=np.concatenate([A[0],A[1]]),np.concatenate([B[0],B[1]])
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
    mu=convlt(M,db+da,d)
    if mu[1].count(mu[1][0])+3>len(mu[1]): 
            return(corr((mu[0],[mu[1][0]]*(len(mu[1])+1)),0))
    else: return(mu)
    
def division(x,y,d=50): #Dividiendo y en x, y/x
    A,B=deepcopy(y),deepcopy(x)
    sg=A[0][0]
    U=(['+',1],[0])
    #d=10
    compl(U,A)
    a=A[0][1:]+A[1]
    u=U[0][1:]+U[1]
    R,A,U=[],'',''
    for k in range(0,len(a)):
        A+=str(int(a[k]))
        U+=str(int(u[k]))
    a,u=int(A),int(U)
    if a==u:
        D=x
        return(multiplicacion(D,B))
    else:
        if a>u:
            R=[0,'.']
        else: 
            R=[u//a,'.']
        res=u%a
        while d>0:
            res=10*res
            R.append(res//a)
            res=res%a
            d-=1
        D=([sg]+list(str(R[0])),R[2:])
    enteros(D)
    return(multiplicacion(D,B))
    #return(R)
    #imprimir(M)


def comparacion(a, b):
    compl(a,b)
    if np.array_equal(a,b)==True: return(True)
    else:print(False)


def pi(n):
    k,R= (['+',1],[0]),[]#Primer término
    for i in range(n+1):
        if i%2==0:f=unidad
        else: f=munidad
        denominador=suma(multiplicacion(enterot(i),enterot(2)),unidad)
        #print(f,denominador);
        termino=multiplicacion(division(f,denominador),enterot(4))
        #print(termino)
        R.append(rmd(termino))
    #print(R)
    M=enterot(0)
    for j in range(len(R)):
        M=suma(M,R[j])
    return(M)
#print(imprimir(pi(2)))
#if __name__    == "__main__":
#    print(imprimir(pi()))