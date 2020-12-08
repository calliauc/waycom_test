#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def generate_calls():
    """return a list of timestamps based on the standard input"""
    calls = []
    for line in sys.stdin:
        call = []
        call += line.split(sep=':')
        call[0] = int(call[0])
        call[1] = int(call[1][:-1])
        calls.append(call)
    return calls



def main():
    calls = generate_calls()
    print(f"{calls}")


main()

# Générer liste avec des int
# 