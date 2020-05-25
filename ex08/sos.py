import sys


morse_code = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}


def set_code(tab):
    buf = ""
    count_str = 0
    count_c = 0
    size_tab = len(tab)
    for str in tab:
        size_str = len(str)
        for c in str:
            if c not in morse_code and c != ' ':
                print(c)
                print("ERROR")
                quit()
            else:
                if c != ' ':
                    buf += morse_code[c]
                    buf += " "
                else:
                    buf += "/ "
            count_c += 1
        if count_str < size_tab - 1:
            buf += "/ "
        count_str += 1
    return buf


def up_case(tab):
    ret = []
    for str in tab:
        ret.append(str.upper())
    return (ret)


def main():
    if len(sys.argv) < 2:
        print("ERROR")
    else:
        tab = up_case(sys.argv[1:])
        buf = set_code(tab)
        print(buf)


if __name__ == "__main__":
    main()
