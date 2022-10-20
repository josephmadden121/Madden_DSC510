# DSC510
# Week 8
# Programming Assignment - 8.1
# Author: Joseph Madden
# Date: 10/19/2022
# The purpose of this program is being able for me to read the file and display the frequency of the words from the file

import string

# function to add word to dictionary and update the count


def add_word(word, word_dict):
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

# function to remove punctuations, space from all the lines


def process_line(line, word_dict):
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, word_dict)

# function to print the length of dictionary and the word frequency


def pretty_print(word_dict):
    word, count = 'Word', 'Count'
    print(f'\n{word:<20}{count}')
    print('-------------------------')
    for key, val in word_dict.items():
        print(f'{key:<20}{val}')

# function to open the file


def main():
    word_dict = {}
    try:
        with open('Gettysburg.txt') as gba_file:
            for line in gba_file:
                process_line(line, word_dict)
        word_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))  # sort the dictionary by count
        print('Length of the dictionary:', len(word_dict))
        pretty_print(word_dict)
    except Exception as ex:
        print('Error Occurred while opening file: ', ex)


if __name__ == '__main__':
    main()
