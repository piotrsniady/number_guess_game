import random
import datetime
import os


class CreateSaveFile:
    def __init__(self):
        self.save_file = "game_history.txt"

    def create(self):
        if not os.path.exists(self.save_file):
            with open(file=self.save_file, mode="w") as f:
                f.close()


class SaveToFile:
    def __init__(self, turn_opt, guess_opt, option_opt):
        self.turn_opt = turn_opt
        self.guess_opt = guess_opt
        self.option_opt = option_opt

    def save(self):
        if not os.path.exists("game_history.txt"):
            CreateSaveFile().create()

        with open("game_history.txt", "a+") as save_file:
            save_file.write("turn: " + str(self.turn_opt) + "\n")
            save_file.write("guess number: " + str(self.guess_opt) + "\n")
            save_file.write("option: " + str(self.option_opt) + "\n")


class WriteLastLine:
    def __init__(self):
        self.last_line = 10 * " # " + "\n"

    def write(self):
        if not os.path.exists("game_history.txt"):
            CreateSaveFile().create()

        with open("game_history.txt", "a+") as save_file:
            save_file.write("game date: " + str(datetime.date.today()) + "\n")
            save_file.write(self.last_line)


class AskForNewGame:
    _answer_opt_ = ["yes", "no"]

    def check_answer(self):
        while True:
            answer = input("Would you like start a new game?: ")
            if answer not in self._answer_opt_:
                print(f"[WARNING] You entered wrong option.\nAvailable options are {self._answer_opt_}.")
                continue
            else:
                if answer == "yes":
                    game()
                else:
                    print("Quitting game.")
                    quit()


def game():
    random_number = random.randint(1, 10)
    to_low = 0
    to_high = 0
    turn = 0

    guess = int(input("Please enter your guess between 1 and 10: "))
    if guess not in range(1, 11):
        print("[WARNING] You entered invalid number. Only numbers from 1 to 10 are available.")
        print("Leaving the game.")
        quit()
    else:
        while random_number != "guess":
            if guess < random_number:
                print("Your guess is too LOW")
                to_low += 1
                turn += 1
                print("to low count:", to_low)
                SaveToFile(turn_opt=turn, guess_opt=guess, option_opt="to_low").save()
                guess = int(input("Please enter your guess between 1 and 10: "))
            elif guess > random_number:
                print("Your guess is too HIGH")
                guess = int(input("Please enter your guess between 1 and 10: "))
                to_high += 1
                turn += 1
                print("to high count:", to_high)
                SaveToFile(turn_opt=turn, guess_opt=guess, option_opt="to_high").save()
            else:
                print("GUESSED")
                guess_count = to_high + to_low + 1
                turn += 1
                SaveToFile(turn_opt=turn, guess_opt=guess, option_opt="guess_count").save()
                print("guess count:", guess_count)
                WriteLastLine().write()

                AskForNewGame().check_answer()
                break


if __name__ == '__main__':
    game()
