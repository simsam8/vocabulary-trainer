from vocab import Vocab
from vocab_tester import Vocab_tester as Tester

FILE_TO_USE = "vocabs.json"
game_tester = Tester(FILE_TO_USE)
vocab = Vocab(FILE_TO_USE)


def interface():
    print("\n- - - - - - - - - - - -")
    print("1.\tAdd word pair")
    print("2.\tTest your vocabulary")
    print("3.\tVocabulary settings")
    print("4.\tChange current vocabulary file")
    print("5.\tSave and Quit")
    print("- - - - - - - - - - - -\n")


def change_file():
    global FILE_TO_USE, game_tester, vocab
    new_file = input("Input file to change to: ")
    FILE_TO_USE = new_file
    game_tester = Tester(FILE_TO_USE)
    vocab = Vocab(FILE_TO_USE)


def main():
    while True:
        interface()
        try:
            choice = int(input("Choose option: "))
        except ValueError:
            print("String is not valid as input")
            continue

        if choice == 1:
            vocab.add_pair()
        if choice == 2:
            game_tester.random_pair()
        if choice == 3:
            vocab.access_vocab()
        if choice == 4:
            change_file()
        if choice == 5:
            print("Saving and Exiting program")
            vocab.save()
            return False
        else:
            print("Not a valid option")


if __name__ == "__main__":
    main()
