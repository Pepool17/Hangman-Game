import functions as f
from os import system 

def run():
    
    list = f.print_men()

    draw = next(list)
    f.print_draw(draw)

    word = f.random_word()
    lines = '_' * len(word)
    life = 6

    try:
        letter = input('Write a letter: ')
        print(letter)
            
        if len(letter) != 1:
            raise ValueError('Write only a letter')
            
        for index in range(len(word)):
            if word[index] == letter:
                lines[index] = letter.upper()
            else:
                life -= 1
                

    except ValueError as ve:
        print(ve)


    '''while True:
        #system('cls')
        f.one_read('title.txt')
        draw = next(list)
        f.print_draw(draw)
        print(word)
        print(f'word: {lines}')
        print(f'Attempts:  {life}')

        try:
            letter = input('Write a letter: ')
            letter = letter.lower()
            print(letter)
            
            if type(int(letter)) == int or len(letter) != 1:
                raise ValueError('Write only a letter')
            
            for index in range(len(word)):
                if word[index] == letter:
                    lines[index] = letter.upper()
                else:
                    life -= 1
                

        except ValueError as ve:
            print(ve) '''              

    

if __name__ == '__main__':
    run()
