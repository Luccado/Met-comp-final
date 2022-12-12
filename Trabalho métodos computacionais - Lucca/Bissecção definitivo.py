def bissection(func, a, b, error_accept):
    """

    :param func: o usuário define a função que deve ser uma string
    :param a: Chute inicial menor
    :param b: Chute inicial maior
    :param error_accept: Critério de parada
    """

    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)



    while error > error_accept:
        c = (b + a) / 2  #método da bisecção

        if f(a) * f(b) >= 0:
            print("Coloque um valor válido")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)
            print('[', ' ', a, ' ', ']', '[', ' ', b, ' ', ']')

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
            print('[', ' ', a, ' ', ']', '[', ' ', b, ' ', ']')



        else:
            print(f"algo deu errado")
            quit()


    print(f"O valor do error é {error}")
    print(f"O ponto baixo é {a} e o alto é {a}")


def data():
    func = str(input("Coloque a função desejada: "))
    a = float(input("coloque o chute inicial menor: "))
    b = float(input("Coloque o chute inicial maior: "))
    error_accept = float(input("coloque o critério de parada: "))
    return bissection(func, a, b, error_accept)


data()




#bissection("(4*x ** 3) + 3*x -3", 0, 1, 0.05) teste