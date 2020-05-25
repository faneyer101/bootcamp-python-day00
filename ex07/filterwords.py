import string
import sys


def remove_small_word(liste, size):
    try:
        size_int = int(size)
    except ValueError:
        print("ERROR")
        quit()
    i = 0
    while i < len(liste):
        if len(liste[i]) <= size_int:
            liste.remove(liste[i])
            i -= 1
        i += 1
    return liste


def remove_punctuation(str):
    for c in string.punctuation:
        str = str.replace(c, '')
    return str


def main():
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        str = remove_punctuation(sys.argv[1])
        liste = remove_small_word(str.split(' '), sys.argv[2])
        if len(liste) == 0:
            print("ERROR")
        else:
            print(liste)


if __name__ == "__main__":
    main()
