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


def random_word():
    dictionary = read()
    word = random.choice(dictionary)
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
    men_array = men()
    array0 = next(men_array)
    array1 = next(men_array)
    array2 = next(men_array)
    array3 = next(men_array)
    array4 = next(men_array)
    array5 = next(men_array)
    array6 = next(men_array)

    if numb == 0:
        print_draw(array0)
    elif  numb == 1:
        print_draw(array1)
    elif numb == 2:
        print_draw(array2)
    elif numb == 3:
        print_draw(array3)
    elif numb == 4:
        print_draw(array4)
    elif numb == 5:
        print_draw(array5)
    else:
        print_draw(array6)

        

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


        



