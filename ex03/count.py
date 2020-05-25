import string


def count_str(str):
    punct = 0
    for c in str:
        if c in string.punctuation:
            punct += 1
    print("The text contains", len(str), "characters:")
    print("-", sum(1 for c in str if c.isupper()), "upper letters")
    print("-", sum(1 for c in str if c.islower()), "lower letters")
    print("-", punct, "punctuation marks")
    print("-", sum(1 for c in str if c.isspace()), "spaces")


def text_analyzer(*args):
    """This function counts the number of upper characters,
lower characters, punctuation and spaces in a given text."""
    if len(args) > 1:
        print("ERROR")
    elif len(args) == 0:
        count_str(input("What is the text to analyse?\n"))
    else:
        count_str(args[0])
