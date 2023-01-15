import json


class Vocab:
    def __init__(self) -> None:
        self.languages = {}

        with open("vocabs.json", "r") as f:
            self.languages = json.load(f)

    def interface(self):
        print("\n- - - - - - - - - - - -")
        print("1.\tAdd Word Pair")
        print("2.\tAdd Language")
        print("3.\tSave")
        print("4.\tQuit")
        print("- - - - - - - - - - - -\n")

    def add_language(self):
        new_lang = input("Language to add: ").lower()
        if new_lang not in self.languages:
            self.languages.update({new_lang: []})
            print(f"{new_lang} added to languages")
        else:
            print(f"{new_lang} is already in languages")
        # print(self.languages)

    def add_pair(self):
        language = input("Choose language: ").lower()
        unknown = input(f"New word in {language}: ").lower()
        known = input("Word in English: ").lower()
        if len(self.languages[language]) == 0:
            pair_id = 0
        else:
            pair_id = len(self.languages[language]) - 1

        pair_data = {
            "id": pair_id,
            "unknown": unknown,
            "known": known,
            "rate": None,
        }

        self.languages[language].append(pair_data)

    def save(self):
        to_write = json.dumps(self.languages, indent=1)
        with open("vocabs.json", "w") as f:
            f.write(to_write)

    def show_data(self):
        print(self.languages)


def main():
    voc = Vocab()
    voc.show_data()
    while True:
        voc.interface()
        choice = int(input("Choose option: "))
        if choice == 1:  # Add word pair
            voc.add_pair()
        if choice == 2:  # Add language
            voc.add_language()
        if choice == 3:  # Save
            voc.save()
        if choice == 4:  # Quit
            return False


if __name__ == "__main__":
    main()
