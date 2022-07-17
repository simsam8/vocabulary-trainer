import json

words = {}
word_pairs = []

# Adding word pairs with an index as key, and pairs as tuple as value
def new_pair():
    unknown = input('Word in English: ').lower()
    known = input('Word in Norwegian: ').lower()
    word_pairs.append((unknown,known))
    print(word_pairs)

       


def interface():
    print('\n- - - - - - - - - - - -')
    print('1.\tAdd word pair\n2.\tSave\n3.\tQuit')
    print('- - - - - - - - - - - -\n')


def main():
    while True:
        interface()
        choice = int(input('Choose option: '))
        if choice == 1:
            new_pair()
        if choice == 2:
            pass
        if choice == 3:
            return False
    
if __name__ == '__main__':
    main()