import functions as f
from os import system 

def run():
    
    list = f.print_men()

    draw = next(list)
    f.print_draw(draw)

    word = f.random_word()
    lines = '_' * len(word)
    life = 6


    while True:
        #system('cls')
        f.one_read('title.txt')
        draw = next(list)
        f.print_draw(draw)
        print(word)
        print(f'word: {lines}')
        print(f'Attempts:  {life}')

        letter = f.into_to_letter()
                        
        for index in range(len(word)):
            if word[index] == letter:
                lines[index] = letter.upper()
            else:
                life -= 1
        
        if life == 0:
            break
                

                
    

if __name__ == '__main__':
    run()
