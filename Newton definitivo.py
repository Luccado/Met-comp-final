import pandas as pd #fazer a tabela ficar bonita
import numpy as np
import matplotlib.pyplot as plt


def Newton(x, y, xi):
    n = len(x) #num de dados
    fdd = [[None for x in range(n)] for x in range(n)] #cria a matriz linhas e colunas
    yint = [None for x in range(n)]


    for i in range(n):
        fdd[i][0] = y[i] #determina onde começa linha 0 coluna 0

    for j in range(1, n): #1 até n priorizando a ordem 1
        for i in range(n - j): # 0 até n-j
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i]) #diferença divididas

    fdd_table = pd.DataFrame(fdd)
    print("Tabela: \n",fdd_table.to_string())
    xterm = 1
    yint = fdd[0][0]


    for order in range(1, n):
        xterm = xterm * (xi - x[order - 1])
        yint = yint + fdd[0][order] * xterm

    return yint



x = [-1, 0, 2] #Dados da tabela
y = [4, 1, -1] #dados do f(x) da tabela
xp = 0.05 #valor desejádo para calcular através de interpolação
yp = Newton(x, y, xp) #interpolação de newton

print('O valor da interpolação é: g(%.3f) = %.3f' % (xp, yp)) #valor interpolação

