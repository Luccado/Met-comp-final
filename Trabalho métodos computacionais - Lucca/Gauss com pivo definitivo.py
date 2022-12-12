import math

def gaussPivoPar(A,b):
    for k in range(len(A)): #Verifica as linhas
        maipiv = math.fabs(A[k][k]) #verificar qual é o maior pivô
        linhaPiv = k
        for l in range(k+1, len(A)):
            if math.fabs(A[l][k]) > maipiv:
                maipiv = math.fabs(A[l][k])
                linPiv = l
        if linPiv != k: #permuta as linhas
            linhaAuxiliar = A[k]
            A[k] = A[linPiv]
            A[linPiv] = linhaAuxiliar

            bAuxiliar = b[k]
            b[k] = b[linPiv]
            b[k] = b[linPiv]
            b[linPiv] = bAuxiliar

        for m in range(k+1, len(A)): #eliminação gaussiana método
            multiplicador = A[m][k] / A[k][k]
            for n in range(k, len(A)):
                A[m][n] -= multiplicador * A[k][n]
            b[m] -= multiplicador * b[k]


    for i in range(len(A)): #printar A escalonada e o vetor b escalonado
        print(A[i])
    print("matriz b: ",b)
    print()
    calculaSolucao(A, b)




def calculaSolucao(A,b):
    vetorSouluccao = []
    for i in range(len(A)):
        vetorSouluccao.append(0)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x -= A[linha][coluna] * vetorSouluccao[coluna]
            coluna -= 1
        x /= A[linha][linha]
        linha -= 1
        vetorSouluccao[coluna] = x

    for j in range(len(vetorSouluccao)):
        print("x" + str(j) + " = " + str(vetorSouluccao[j]))


gaussPivoPar([[2,4,3],[1,2,2],[4,4,3]],[1,11,3])