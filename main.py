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
    # TODO: add function to change file
    print("4.\tChange current vocabulary file")
    print("5.\tQuit")
    print("- - - - - - - - - - - -\n")


def main():
    while True:
        interface()
        choice = int(input("Choose option: "))

        if choice == 1:
            vocab.add_pair()
        if choice == 2:
            game_tester.random_pair()
        if choice == 3:
            vocab.access_vocab()
        if choice == 4:
            return
        if choice == 5:
            print("Exiting program")
            return False


if __name__ == "__main__":
    main()
