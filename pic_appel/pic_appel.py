#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def clean_call(call):
    """Convert data to integers and remove newlines"""
    call[0] = int(call[0])
    call[1] = int(call[1][:-1])
    return call

def generate_calls():
    """Return a list of calls's timestamps from the standard input"""
    calls = []
    for line in sys.stdin.readlines():
        call = []
        call += line.split(sep=':')
        calls.append(clean_call(call))
    return calls

def count_current_calls(begin, calls):
    """Searching for any other calls still in progress at the beginning of a call"""
    counter = 0
    for call in calls:
        if call[1] >= begin:
            counter +=1
    return counter

def process_calls(calls):
    """For each call in reverse chronological order, check how many calls are in progress.
    Saves the highest number of simultaneous calls as peak value."""
    peak = 0
    for call in reversed(calls):
        counter = count_current_calls(call[0], calls)
        if peak < counter:
            peak = counter
        calls.pop(-1)
        return peak

def print_calls_peak(peak):
    """Print only peak value on standard output."""
    sys.stdout.write(f"{peak}\n")

def main():
    calls = generate_calls()
    peak = process_calls(calls)
    print_calls_peak(peak)


main()
