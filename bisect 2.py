def bissection(func, a, b, error_accept):
    """

    :param func: o usuário define a função que deve ser uma string
    :param a: Chute inicial menor
    :param b: Chute inicial maior
    :param error_accept: Critério de parada
    :return:
    """


    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)

    while error > error_accept:
        c = (b + a) / 2  #método da bisecção

        if f(a) * f(b) >= 0:
            print("num vai rolar")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)

        else:
            print(f"algo deu errado")
            quit()


    print(f"the error is {error}")
    print(f"the low pont {a} e o alto {a}")

bissection("(4*x ** 3) + 3*x -3", 0, 1, 0.05)