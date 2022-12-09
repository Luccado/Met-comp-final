x = 6 #chute inicial
tol = 0.5 # critério de parada
num_iter = 20 # número máximo de iteração

def funct(x):
    f_x = (x**3) - (x**2) + x - 5 # x^3 - x^2 + x - 5
    return f_x

def dfunct(x):
    small_val = 1E-2
    df_dx = (funct(x+small_val) - funct(x-small_val)) / (small_val*2)
    return df_dx

for i in range(1, num_iter, 1):
    f_x = funct(x)
    df_dx = dfunct(x)
    print(str(i) + ' x:' + str(x) + 'f(x): ' + str(f_x))
    if abs(f_x) < tol:
        break
    x = x - f_x/df_dx

    print('Seu "zero" está situado em ' + str(x) + ' f(x): ' + str(f_x))
    print('Houve ' + str(i) + ' iterações até aqui')