import json
import error_msgs as ERR


class Vocab:
    def __init__(self, file_to_load) -> None:
        self.file_to_load = file_to_load
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
            print("3.\tEdit Pair")
            print("4.\tRemove Pair")
            print("5.\tRemove Language")
            print("6.\tSave and Quit")
            print("7.\tQuit")
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
            print(f"{len(self.languages[language])}.\tCancel")
            print("\n- - - - - - - - - - - -")

    def add_language(self):
        new_lang = input("Language to add: ").lower()
        if new_lang not in self.languages:
            self.languages.update({new_lang: []})
            print(f"{new_lang} added to languages")
        else:
            print(f"{new_lang} is already in languages")

    def choose_language(self):
        while True:
            self.interface("language")
            try:
                lang_id = int(input("Choose language: ").lower())
                if lang_id >= len(self.languages):
                    print(ERR.NO_OPTION)
                    continue
                language = list(self.languages.items())[lang_id][0]
                return language
            except ValueError:
                print(ERR.STR_NOT_VAL_INP)

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
            "correct": 0,
            "total": 0,
        }

        self.languages[language].append(pair_data)
        self.save()

    def remove_pair(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            return
        language = self.choose_language()
        while True:
            try:
                self.interface("pairs", language=language)
                to_remove = int(input("Choose a pair to remove: "))
                if to_remove > len(self.languages[language]):
                    print(ERR.NO_OPTION)
                    continue
                if to_remove == len(self.languages[language]):
                    print("Cancelling pair removal")
                    break
                self.languages[language].pop(to_remove)
                print("Pair succesfully removed!")
                break

            except ValueError:
                print(ERR.STR_NOT_VAL_INP)
                continue

    def edit_pair(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            return
        language = self.choose_language()
        while True:
            try:
                self.interface("pairs", language=language)
                pair_id = int(input("Choose a pair to edit: "))
                to_edit = self.languages[language][pair_id]
                if pair_id > len(self.languages[language]):
                    print(ERR.NO_OPTION)
                    continue
                if pair_id == len(self.languages[language]):
                    print("Cancelling pair editing")
                    break
                print(f"0.\tunknown: {to_edit['unknown']}")
                print(f"1.\tknown: {to_edit['known']}")
                edit_option = int(input(("Choose option to edit: ")))
                while True:
                    if edit_option == 0:
                        old_text = "unknown"
                        break
                    elif edit_option == 1:
                        old_text = "known"
                        break
                    else:
                        print(ERR.NO_OPTION)
                new_text = input("Write your edit: ")
                self.languages[language][pair_id][old_text] = new_text
                print("Pair succesfully edited!")
                break

            except ValueError:
                print(ERR.STR_NOT_VAL_INP)
                continue

    def remove_language(self):
        if len(self.languages) == 0:
            print("No languages exist!")
            return
        language = self.choose_language()
        self.languages.pop(language)
        print(f"{language} succesfully removed")

    def save(self):
        to_write = json.dumps(self.languages, indent=1)
        with open(self.file_to_load, "w") as f:
            f.write(to_write)

    def load(self):
        with open(self.file_to_load, "r") as f:
            self.languages = json.load(f)

    def show_data(self):
        print(self.languages)

    def access_vocab(self):
        while True:
            self.show_data()
            self.interface("main")
            choice = int(input("Choose option: "))
            if choice == 1:  # Add word pair
                self.add_pair()
            elif choice == 2:  # Add language
                self.add_language()
            elif choice == 3:  # Edit pair
                self.edit_pair()
            elif choice == 4:  # Remove pair
                self.remove_pair()
            elif choice == 5:  # Remove language
                self.remove_language()
            elif choice == 6:  # Save and Quit
                self.save()
                return False
            elif choice == 7:  # Quit without saving
                return False
            else:
                print(ERR.NO_OPTION)


if __name__ == "__main__":
    voc = Vocab("vocabs.json")
    voc.access_vocab()
