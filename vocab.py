
class Vocab:
    def __init__(self) -> None:
        self.languages = {}
        
    
    def interface(self):
        print('\n- - - - - - - - - - - -')
        print('1.\tAdd Word Pair')
        print('2.\tAdd Language')
        print('3.\tSave')
        print('4.\tQuit')
        print('- - - - - - - - - - - -\n')
            
    def add_language(self):
        new_lang = input('Language to add: ').lower()
        if new_lang not in self.languages:
            self.languages.update({new_lang: []})
            print(f'{new_lang} added to languages')
        else:
            print(f'{new_lang} is already in languages')
        #print(self.languages)


def main():
    voc = Vocab()
    while True:
        voc.interface()
        choice = int(input('Choose option: '))
        if choice == 1:
            pass
        if choice == 2:
            voc.add_language()
        if choice == 3:
            pass
        if choice == 4:
            return False

if __name__ == '__main__':
    main()