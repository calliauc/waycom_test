#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def generate_text():
    """return a list of words based on the standard input"""
    text = f""
    for line in sys.stdin:
        text += line
    return text.split()

def search_other_occurence(word_to_count, split_text):
    """If the word has more than one occurrence, each are found and removed from the list."""
    counter = 1
    while word_to_count in split_text:
        for i, word in enumerate(split_text):
            if word == word_to_count:
                counter += 1
                split_text.pop(i)
    return counter

def process_text(split_text):
    """Remove the first word from the list and check any other occurrence"""
    counter_dict = dict()
    while len(split_text):
        word_to_count = split_text.pop(0)
        counter = 1
        if word_to_count in split_text:
            counter = search_other_occurence(word_to_count, split_text)
        counter_dict[word_to_count] = counter
    return counter_dict

def sort_dict(counter_dict):
    """From the dictionary, return a list of tuples with the words and counters.
    Tuples are sorted by decreasing counters values"""
    return sorted(counter_dict.items(), key=lambda t: t[1], reverse=True)

def print_dict(counter_dict):
    """Print on standard output words and their occurrences"""
    for line in counter_dict:
        sys.stdout.writelines(f"{line[1]} {line[0]}\n")
        # print(f"{line[1]} {line[0]}")


def main():
    split_text = generate_text()
    counter_dict = process_text(split_text)
    counter_dict = sort_dict(counter_dict)
    print_dict(counter_dict)
    exit(0)


main()
