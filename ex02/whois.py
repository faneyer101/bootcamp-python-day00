import sys


def verif_number(number):
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    if len(sys.argv) == 1:
        quit()
    elif len(sys.argv) > 2:
        print("ERROR")
    elif not sys.argv[1].isnumeric():
        print("ERROR")
    else:
        verif_number(int(sys.argv[1]))


if __name__ == "__main__":
    main()
