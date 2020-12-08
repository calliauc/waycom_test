#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def generate_text():
    text = f""
    for line in sys.stdin:
        text += line

    return text.split()

def process_text(split_text):
    counter_dict = dict()
    while len(split_text):
        word_to_count = split_text.pop(0)
        counter = 1
        if word_to_count in split_text:
            while word_to_count in split_text:
                for i, word in enumerate(split_text):
                    if word == word_to_count:
                        counter += 1
                        split_text.pop(i)
        counter_dict[word_to_count] = counter
    return counter_dict

def sort_dict(counter_dict):
    return sorted(counter_dict.items(), key=lambda t: t[1], reverse=True)

def print_dict(counter_dict):
    for line in counter_dict:
        print(f"{line[1]} {line[0]}")


def main():
    split_text = generate_text()
    counter_dict = process_text(split_text)
    counter_dict = sort_dict(counter_dict)
    print_dict(counter_dict)
    exit(0)

main()


# Regarder le premier mot
# Le supprimer
# Chercher s'il est encore dans le tableau
# Si oui, incrémenter et le supprimer
# Si non ou absent, passer au mot suivant
