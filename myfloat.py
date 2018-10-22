import myfloat_func as my
class MyFloat:

    def __init__(self,t):
        if type(t) is int:
            self.t=my.enterot(t)
        elif type(t) is float:
            self.t=my.enterot(int(t//1))
            self.t=(self.t[0],list(str(t-t//1)[2:]))
            my.enteros(self.t)
        else:
            self.t=t

    def __add__(self,other):
        return(MyFloat(my.suma(self.t,other)))

    def __sub__(self,other):
        return(MyFloat(my.resta(self.t,other)))

    def __mul__(self,other):
        return(MyFloat(my.multiplicacion(self.t,other)))

    def __div__(self,other):
        return(MyFloat(my.multiplicacion(self.t,other)))

    def __radd__(self,other):
        return(MyFloat(my.suma(other,self.t)))

    def __rsub__(self,other):
        return(MyFloat(my.resta(other,self.t)))

    def __rmul__(self,other):
        return(MyFloat(my.multiplicacion(other,self.t)))

    def __rdiv__(self,other):
        return(MyFloat(my.multiplicacion(other,self.t)))

    def __str__(self):
        return(my.imprimir(self.t))

    def __repr__(self):
        return(my.imprimir(self.t))

    def __eq__(self,other):
         return(my.comparacion(self.t,other))

    def __ne__(self,other):
         return(my.comparacion(self.t,other))

if __name__ == "__main__":
    a=MyFloat((['+',1],[0]))
    b=MyFloat((['+',4],[0]))
    print(a+b)