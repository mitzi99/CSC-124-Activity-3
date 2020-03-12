#Mitzi V. Dorato
#BSCS-II
#2018-5849


import matplotlib.pyplot as plt
import math


x_log = []
y_log = []

x_linearithmic = []
y_linearithmic = []

x_linear = []
y_linear = []

x_quadratic = []
y_quadratic = []

x_poly =[]
y_poly = []

x_expo = []
y_expo = []


def log():

    n = int(input("Enter value of n > "))
    x_log.append(n)
    log_base = 10

    if n < 0:
        print("Error")

    if n == 0:
        print("Error")

    else:
        operation_log = math.log(int(n), int(log_base))
        print(operation_log)
        y_log.append(operation_log)
        #print(ylog)
        print("---------------------------------------------------")


def linearithmic():

    n = int(input("Enter value of n for linearithmic > "))
    x_linearithmic.append(n)

    if n < 0:
        print("Error")

    if n == 0:
        print("Error")

    else:
        log_of_n = math.log(int(n), 10)
        linearithmic_operation = n * log_of_n
        print(linearithmic_operation)
        y_linearithmic.append(linearithmic_operation)
        #print(ylinearithmic)
        print("---------------------------------------------------")


def linear():
    n = int(input("Enter value of n for linear > "))
    x_linear.append(n)
    y_linear.append(n)
    print("---------------------------------------------------")


def quadratic():
    n = int(input("Enter value of n for quadratic > "))
    x_quadratic.append(n)
    quad = n ** 2
    print(quad)
    y_quadratic.append(quad)
    print("---------------------------------------------------")


def polynomial():
    n = int(input("Enter value of n for polynomial > "))
    x_poly.append(n)
    poly = n ** 3
    print(poly)
    y_poly.append(poly)
    print("---------------------------------------------------")


def exponential():
    constant = 2
    n = int(input("Enter value of n for the exponent > "))
    x_expo.append(n)
    expo = constant ** n
    print(expo)
    y_expo.append(expo)
    print("---------------------------------------------------")


def main():
    print("---------------------------------------------------")
    print("1 Logarithmic")
    print("2 Linearithmic")
    print("3 Linear")
    print("4 Quadratic")
    print("5 Polynomial")
    print("6 Exponential")

    choice = input("Enter choice > ")

    if choice == '1':
        log()
        print("Show graph?\n1. Yes\n2. No")
        option = input(" > ")
        if option == '1':
            plt.plot(x_log, y_log)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option == '2':
            main()

    if choice == '2':
        linearithmic()
        print("Show graph?\n1. Yes\n2. No")
        option2 = input(" > ")
        if option2 == '1':
            plt.plot(x_linearithmic, y_linearithmic)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option2 == '2':
            main()

    if choice == '3':
        linear()
        print("Show graph?\n1. Yes\n2. No")
        option3 = input(" > ")
        if option3 == '1':
            plt.plot(x_linear, y_linear)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option3 == '2':
            main()

    if choice == '4':
        quadratic()
        print("Show graph?\n1. Yes\n2. No")
        option4 = input(" > ")
        if option4 == '1':
            plt.plot(x_quadratic, y_quadratic)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option4 == '2':
            main()

    if choice == '5':
        polynomial()
        print("Show graph?\n1. Yes\n2. No")
        option5 = input(" > ")
        if option5 == '1':
            plt.plot(x_poly, y_poly)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option5 == '2':
            main()

    if choice == '6':
        exponential()
        print("Show graph?\n1. Yes\n2. No")
        option6 = input(" > ")
        if option6 == '1':
            plt.plot(x_expo, y_expo)
            plt.xlabel("Value of n")
            plt.ylabel("Behavior")
            plt.title("Asymptotic Analysis")
            plt.show()
            main()
        if option6 == '2':
            main()

main()
