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


def run():



if __name__ == '__main__':
    run()








