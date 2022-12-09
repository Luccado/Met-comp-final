import matplotlib.pyplot as plt
import numpy as np
import math


#fazer função input
def f(x):
  return np.power(x,3) - 9*x + 3 #função escolhida x^3 - 9x + 3

def df(x):
  return 3*np.power(x,2) - 9 #função derivada


x = np.arange(-5.0, 20.0, 0.1) #range

#gráfico
plt.figure()
plt.grid()
plt.plot(x, f(x),'b-')

x0 = 1.5 #valor inicial
eps1 = 0.001 #precisão eixo x - critério de parada
eps2 = eps1 #precisão eixo y
maxiter = 20 #nº max de interações
lista   = [x0] #armazena os valores aqui
iter    = 0 #quantidade de interações

while (math.fabs(f(x0))>eps1)&(iter<=maxiter):
  print('[',x0,']')
  xk = x0 - f(x0)/df(x0) #função de interação
  lista.append(xk) #adicionando cada valor novo na lista
  if (math.fabs(f(x0))<eps1)|(math.fabs(xk-x0)<eps2): #
    break;
  else:
    x0 = xk
  iter = iter + 1 #atualizando o valor da interação

cont = 0
for x in lista: #para imprimir bolinhas vermelhas no gráfico
  plt.plot(x,f(x),'ro')
  name = '$x_'+str(cont)+'$'
  plt.text(x,0.1*f(x),name,fontsize=12)
  cont = cont + 1
plt.show()

print('[',xk,']')
print('Número de iterações: ',iter)
print('Precisao |f(xk)|: ',math.fabs(f(xk)))
print('Precisao |xk-x0|: ',math.fabs(xk-x0)) #precisão xk em relação ao ponto anterior