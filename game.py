import functions as f
from os import system 

def run():
    
    word = f.random_word()
    lines = list('_' * len(word))
    life = 6
    numb = 0

    while True:
        system('cls')
        f.print_only_one_draw('title.txt')
        f.print_men(numb)
        f.print_draw(word)
        print('')
        print('word: ', end = '')
        f.print_draw(lines)
        print('')
        print(f'Attempts:  {life}')

        letter = f.into_to_letter()

        if letter in word:

            
            for index in range(len(word)):
                if word[index] == letter:
                    lines[index] = letter.upper()

            if list(map(lambda x: x.upper(),word)) == lines:
                system('cls')
                print('\t  GANASTE\n')
                print(f'La parabra era: ', end='')
                f.print_draw(list(map(lambda x: x.upper(),word)))
                print('')
                f.print_only_one_draw('pikachu.txt') 
                break

        else:
            if life == 1:
                system('cls')
                print('\nYOU LOST')
                break
            life -= 1
            numb += 1
    

if __name__ == '__main__':
    run()
