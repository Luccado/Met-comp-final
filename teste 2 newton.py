import math

def f(x):
    return (x*x - x - 2.0)

def df(x):
    h = 0.000001
    return((f(x + h) - f(x))/h)

TOL = 0.00001
N0 = 100 #interações
x0 = float(input("Entre com a aproximação inicial: "))
x = 0.0

i = 1

while(math.fabs(f(x0)) > TOL):

    x = x0 - f(x0)/df(x0)
    x0 = x
    i = i + 1
    if(i >= N0):
        print("ATENÇÃO: RAÍZ NÃO ENCONTRADA")
        break

if(i < N0):
    print("\n\nRaíz %f\nInterações: %f\nf(%f) = %f\n\n"%(x0,i,x0,f(x0)))