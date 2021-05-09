import pandas as pd
import numpy as np
import csv
import random
import re

def read():
    with open('Letters\letter_data_base.csv', encoding = 'utf8') as f:
        datos = csv.reader(f, delimiter=',')
        for line in datos:
            values = line
        return values


def normalize(word):
    replacements = (
        ('á', 'a'),
        ('é', 'e'),
        ('í', 'i'),
        ('ó', 'o'),
        ('ú', 'u'),
    )
    for a, b in replacements:
        word = word.replace(a, b)

    return word 


def random_word():
    dictionary = read()
    word = random.choice(dictionary)
    word = normalize(word)
    return list(word)


def men(name = 'men.txt'):
    try:
            
        with open(name, 'r', encoding = 'utf8') as man:
            for _ in range(7):
                draw = []
                for _ in range(19):
                    line = man.readline()
                    draw.append(line)
                yield draw
                
    except FileNotFoundError:
        print("Error : The file isn't found" )


def print_draw(draw):
    for line in draw:
        print(line, end = '')


def print_men(numb):
    men_word = men()
    word0 = next(men_word)
    word1 = next(men_word)
    word2 = next(men_word)
    word3 = next(men_word)
    word4 = next(men_word)
    word5 = next(men_word)
    word6 = next(men_word)

    if numb == 0:
        print_draw(word0)
    elif  numb == 1:
        print_draw(word1)
    elif numb == 2:
        print_draw(word2)
    elif numb == 3:
        print_draw(word3)
    elif numb == 4:
        print_draw(word4)
    elif numb == 5:
        print_draw(word5)
    else:
        print_draw(word6)

        

def print_only_one_draw(name):
    try:
        with open(name, 'r', encoding = 'utf8') as f:
            archive = f.readlines()
            for line in archive:
                print(line, end = '')
            print('\n')
    except FileNotFoundError:
        print("Error : The file isn't found" )
    
    
def into_to_letter():
    try:
        letter = input('Write a letter: ')

        if len(letter) != 1 or re.match("[0-9]", letter):
            raise ValueError('Write only a letter')

        return letter.lower()
            
    except ValueError as ve:
        print(f'\n{ve}')
        return False


        



    