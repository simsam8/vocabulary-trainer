import json
from random import randrange


class Vocab_tester:
    """
    Takes a json file with vocabulary to test
    """

    def __init__(self, file_to_load):
        self.file_to_load = file_to_load
        self.vocabulary = {}
        self.language = "spanish"
        self.load()

    def load(self):
        with open(self.file_to_load, "r") as f:
            self.vocabulary = json.load(f)

    # TODO: add method to choose random pair
    def random_pair(self):
        random_index = randrange(0, len(self.vocabulary[self.language]))
        pair = self.vocabulary[self.language][random_index]
        fifty_fifty = randrange(0, 2)
        if fifty_fifty == 0:
            display_word = pair["unknown"]
            guess_word = pair["known"]
        elif fifty_fifty == 1:
            display_word = pair["known"]
            guess_word = pair["unknown"]

        user_guess = input(f"Write the translation of {display_word}: ")
        if user_guess == guess_word:
            print("Correct!")
        else:
            print("Wrong!")


# test = Vocab_tester("vocabs.json")
# test.random_pair()
