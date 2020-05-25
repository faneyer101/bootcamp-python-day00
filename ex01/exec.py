import sys


def reverse_letters(s):
    return s[::-1]


def rev(str):
    str = reverse_letters(str)
    str = str.swapcase()
    return str


def main():
    txt = ""
    for key in sys.argv[1:]:
        txt += key + " "
    print(rev(txt[:-1]))


if __name__ == "__main__":
    main()
