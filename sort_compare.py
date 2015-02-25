#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Benchmarking sorting algorithms"""

import time
import random

def insertion_sort(a_list):
    """Performs an insertion sort on a list

    Args: a_list (List): a list to be sorted

    Ex: > a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        > insertion_sort(a_list)
    """

    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    length = end - start
    return (length, a_list)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def shell_sort(a_list):
    """Performs a shell sort on a list

    Args: a_list (List): a list to be sorted

    Ex: > a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        > shell_sort(a_list)
    """

    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time()
    length = end - start
    return (length, a_list)


def python_sort(a_list):
    """Wrapper for Python .sort() function"""
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    length = end - start
    return (length, a_list)


def rand_list(length):
    randlist = []
    for item in range(length):
        randlist.append(random.randint(1,length))
    return randlist


def main():
    """The main function of the program. Runs automatically"""

    tests = [500,1000,10000]
    for test in tests:
        counter = 100
        results = [0,0,0]
        while counter > 0:
            randlist = rand_list(test)
            results[0] += insertion_sort(randlist)[0]
            results[1] += shell_sort(randlist)[0]
            results[2] += python_sort(randlist)[0]
            counter -= 1
        print "For list of {}: ".format(test)
        print "Insertion Sort took %10.7f seconds to run, on average" % \
              (results[0] / 100)
        print "Shell Sort " + \
                "took %10.7f seconds to run, on average" % \
              (results[1] / 100)
        print "Python Sort " + \
                "took %10.7f seconds to run, on average" % \
              (results[2] / 100)

if __name__ == "__main__":
    main()

