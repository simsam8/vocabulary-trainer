import json


class Vocab_tester:
    """
    Takes a json file with vocabulary to test
    """

    def __init__(self, vocabulary):
        self.file_to_load = vocabulary
        self.vocabulary = {}
        self.load()

    def load(self):
        with open(self.file_to_load, "r") as f:
            self.vocabulary = json.load(f)

    def random_pair(self):
        return


test = Vocab_tester("vocabs.json")
