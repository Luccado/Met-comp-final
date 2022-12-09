import numpy as np
import math
import matplotlib.pyplot as plt


def NewtonsMethod(x0, E, imax):
    i = 1
    print(" iteration    approximation")
    while i < imax:

        root = x0 - (f(x0) / fp(x0))

        format_i = "{:6.0f}".format(i)
        format_root = "{:18.8f}".format(root)
        print(format_i, ", ", format_root)
        if (abs(1 - x0 / root) < E):
            return
        x0 = root
        i += 1

    print("failed to converge in ", imax, " iterations")


def f(x):
    output = np.cos(x + math.sqrt(2)) + ((x * x) / 2) + math.sqrt(2) * x
    return output


def fp(x):
    output = -1 * np.sin(x + math.sqrt(2)) + x + math.sqrt(2)
    return output


def main():
    print("This is a program to utilize Newton's Method given a function f, derivative of the\
          function fp, x0, epsilon E, and imax\n To change the functions f and fp, edit\
              directly within the program")

    x0 = int(input("Enter value for x0: "))
    E = float(input("Enter value for E: "))
    imax = int(input("Enter value for imax: "))

    x = np.arange(-7, 5.01, 0.01)
    y = f(x)
    plt.plot(x, y)

    NewtonsMethod(x0, E, imax)


if __name__ == "__main__":
    main()