import sys


def print_error(type_error):
    if type_error == 1:
        print("InputError: only numbers\n")
    elif type_error == 3:
        print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")


def calculate(a, b):
    try:
        nb1 = int(a)
        nb2 = int(b)
    except ValueError:
        print_error(1)
        quit()
    print("Sum:       ", nb1 + nb2)
    print("Difference:", nb1 - nb2)
    print("Product:   ", nb1 * nb2)
    try:
        print("Quotient:  ", nb1 / nb2)
        print("Remainder: ", nb1 % nb2)
    except ZeroDivisionError:
        print("Quotient:   ERROR (div by zero)")
        print("Remainder:  ERROR (modulo by zero)")


def main():
    if len(sys.argv) < 3:
        print_error(0)
    elif len(sys.argv) > 3:
        print_error(3)
    else:
        calculate(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
