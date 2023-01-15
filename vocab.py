import json


class Vocab:
    def __init__(self) -> None:
        self.languages = {}
        self.load()

    def interface(self, interface_type, language=None):
        """
        Available arugments,
        main: prints the main menu
        language: prints available languages
        pairs: displays all pairs in a language with id
        """

        # Main Menu
        if interface_type == "main":
            print("\n- - - - - - - - - - - -")
            print("1.\tAdd Word Pair")
            print("2.\tAdd Language")
            print("3.\tRemove Pair")
            print("4.\tRemove Language")
            print("5.\tSave and Quit")
            print("6.\tQuit")
            print("- - - - - - - - - - - -\n")

        # Display languages
        elif interface_type == "language":
            print("\n- - - - - - - - - - - -")
            for i, language in enumerate(self.languages):
                print(f"{i}.\t{language}")
            print("\n- - - - - - - - - - - -")

        # Display pairs in given language
        elif interface_type == "pairs":
            print("\n- - - - - - - - - - - -")
            for i, pair in enumerate(self.languages[language]):
                pair_id = i
                unknown = pair["unknown"]
                known = pair["known"]
                print(f"{pair_id}.\t{unknown}|{known}")
            print("\n- - - - - - - - - - - -")

    def add_language(self):
        new_lang = input("Language to add: ").lower()
        if new_lang not in self.languages:
            self.languages.update({new_lang: []})
            print(f"{new_lang} added to languages")
        else:
            print(f"{new_lang} is already in languages")

    def choose_language(self):
        self.interface("language")
        lang_id = int(input("Choose language: ").lower())
        language = list(self.languages.items())[lang_id][0]
        return language

    def add_pair(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            print("Add a language to add pairs")
            return

        language = self.choose_language()
        unknown = input(f"New word in {language}: ").lower()
        known = input("Word in English: ").lower()
        # if len(self.languages[language]) == 0:
        #     pair_id = 0
        # else:
        #     pair_id = len(self.languages[language])

        pair_data = {
            #    "id": pair_id,
            "unknown": unknown,
            "known": known,
            "rate": None,
        }

        self.languages[language].append(pair_data)

    def remove_pair(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            return
        language = self.choose_language()
        self.interface("pairs", language=language)
        to_remove = int(input("Choose a pair to remove: "))
        self.languages[language].pop(to_remove)
        print("Pair succesfully removed!")

    def remove_language(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            return
        language = self.choose_language()
        self.languages.pop(language)
        print(f"{language} succesfully removed")

    def save(self):
        to_write = json.dumps(self.languages, indent=1)
        with open("vocabs.json", "w") as f:
            f.write(to_write)

    def load(self):
        with open("vocabs.json", "r") as f:
            self.languages = json.load(f)

    def show_data(self):
        print(self.languages)


def main():
    voc = Vocab()
    while True:
        voc.show_data()
        voc.interface("main")
        choice = int(input("Choose option: "))
        if choice == 1:  # Add word pair
            voc.add_pair()
        if choice == 2:  # Add language
            voc.add_language()
        if choice == 3:  # Remove pair
            voc.remove_pair()
        if choice == 4:  # Remove language
            voc.remove_language()
        if choice == 5:  # Save and Quit
            voc.save()
            return False
        if choice == 6:  # Quit without saving
            return False


if __name__ == "__main__":
    main()
