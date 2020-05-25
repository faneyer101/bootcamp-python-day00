languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }


def main():
    for lang, name in languages.items():
        print("{} was created by {}".format(lang, name))


if __name__ == "__main__":
    main()
