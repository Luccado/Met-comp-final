def newtonMetodo():
    quant_pontos = int(input("Quantidade de elementos na tabela: "))
    elem, felem = [], [] #guarda x e f(x)
    tab = [] #guarda a tabela da diferenças divididas
    for i in range(quant_pontos):
        pontox = float(input("x%d= " %i)) #x
        fpontox = float(input("f(x%d)= " %i)) #f(x)
        elem.append(pontox) #joga o valor na lista
        felem.append(fpontox) #joga o valor de f(x) na lista
    tab.append(felem) #oredem 0

    x = float(input("Ponto x a ser estimado: "))

    step = 1

    for n in range(quant_pontos - 1): #quantidade -1
        ordem = []
        for m in range(len(tab[n]) - 1):
            diferenDiv = (tab[n][m + 1] - tab[n][m] / (elem)[m + step] - elem[m]) #método. dado baixo menos o de cima dividido pelo x de baixo menos o de cima
            ordem.append(diferenDiv) #joga valor na lista ordem
        tab.append(ordem) #joga ordem dentro da tabela
        step += 1


    for l in range(len(tab)):
        print("Ordem %d " %l, tab[l])


    polin = 0
    mult = 0


    for i in range(len(tab)): #acessando a tabela das diferenças divididas
        elem1 = tab[i][0]
        for j in range(mult): #controla a quantidade de multiplicações
            elem1 *= (x - elem[j])
        mult += 1
        polin += elem1
    print("A aproximação encontrada para f(%f)= %f" %(x,polin))

newtonMetodo()