import matplotlib.pyplot as plt
import numpy as np

"""

"""

def f(x):
    return np.log10(x) * x - 1


x = np.arange(1.0, 3.0, 0.1)

# parâmetro de entrada - Intervalo inicial
b = 3.0 #limitante superior
a = 1.0 #limitante inferior
eps = 0.1 #precisão critério de parada
iter = 0
xk = []

while ((b - a) > eps) & (iter <= 20):
    print('[', a, ',', b, ']')
    x0 = (b + a) / 2
    xk.append(x0)
    # Novo intervalo: [Newton's Method, x0]
    if f(x0) * f(b) > 0:
        b = x0
    # Novo intervalo: [x0, b]
    else:
        a = x0
    iter = iter + 1

plt.figure()
plt.grid()
plt.plot(x, f(x), 'b-')

cont = 0
for x in xk:
    plt.plot(x, f(x), 'ro')
    name = '$x_' + str(cont) + '$'
    plt.text(x, 0.1 * f(x), name, fontsize=12)
    cont = cont + 1

print('[', a, ',', b, ']')
plt.show()
