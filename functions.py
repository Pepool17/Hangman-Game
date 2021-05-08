import pandas as pd
import numpy as np
import csv
import random

def read():
    with open('Letters\letter_data_base.csv', encoding = 'utf8') as f:
        datos = csv.reader(f, delimiter=',')
        for line in datos:
            values = line
        return values


def random_word():
    dictionary = read()
    word = random.choice(dictionary)
    return word


def print_men(name = 'men.txt'):
    try:
        draw = []    
        with open(name, 'r', encoding = 'utf8') as man:
            for _ in range(7):
                for _ in range(19):
                    line = man.readline()
                    draw.append(line)
                yield draw
            
    except FileNotFoundError:
        print("Error : The file isn't found" )
        

def one_read(name):
    try:
        with open(name, 'r', encoding = 'utf8') as f:
            archive = f.readlines()
            for line in archive:
                print(line)

    except FileNotFoundError:
        print("Error : The file isn't found" )
    

def run():
    one_read('title.txt') 
    list = print_men()
    draw = next(list)
    for line in draw:
        print(line)


if __name__ == '__main__':
    run()








