from random import randint
import sys


def game():
    count_try = 1
    secret = str(randint(1, 99))
    msg_of_game = "What's your guess between 1 and 99?\n>> "
    ult = "The answer to the ultimate question of life"
    ult_bis = ult + ", the universe and everything is 42."
    while 1:
        res = input(msg_of_game)
        if res == "exit":
            print("Goodbye!")
            quit()
        elif not res.isnumeric():
            print("That's not a number.")
        else:
            if int(res) == int(secret):
                if secret == 42:
                    print(ult_bis)
                if count_try == 1:
                    print("Congratulations! You got it on your first try")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in " + str(count_try) + " attempts!")
                quit()
            elif int(res) < int(secret):
                print("Too low!")
            elif int(res) > int(secret):
                print("Too high!")
            count_try += 1


def main():
    one = "This is an interactive guessing game!"
    two = "You have to enter a number between 1"
    two_bis = two + "and 99 to find out the secret number."
    three = "Type 'exit' to end the game."
    four = "Good luck!"
    print(one + "\n" + two_bis + "\n" + three + "\n" + four + "\n")
    game()


if __name__ == "__main__":
    main()
