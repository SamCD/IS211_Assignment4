#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4"""

import time
import random

def sequential_search(a_list, item):
    """Performs a sequential search on a list

    Args: a_list (List): list to be searched
          item (int): number to be searched for

    Ex: > test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        > print sequential_search(test_list, 3)
        False
    """
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    length = end - start
    return [length, found]


def ordered_sequential_search(a_list, item):
    """Performs an ordered sequential search on a list

    Args: a_list (List): List to be searched
          item (int): number to be searched for

    Ex: > test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        > print ordered_sequential_search(test_list, 3)
        False
    """

    start = time.time()
    a_list.sort()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    length = end - start
    return [length, found]


def binary_search_iterative(a_list, item):
     """Performs an iterative binary search on a list

    Args: a_list (List): List to be searched
          item (int): number to be searched for

    Ex: > test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        > print binary_search_iterative(test_list, 3)
        False
    """
     start = time.time()
     a_list.sort()
     first = 0
     last = len(a_list) - 1
     found = False
     while first <= last and not found:
         midpoint = (first + last) // 2
         if a_list[midpoint] == item:
             found = True
         else:
             if item < a_list[midpoint]:
                 last = midpoint - 1
             else:
                 first = midpoint + 1
     end = time.time()
     length = end - start
     return [length, found]


def binary_search_recursive(a_list, item):
    """Performs a recursive binary search on a list

    Args: a_list (List): List to be searched
          item (int): number to be searched for

    Ex: > test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        > print binary_search_recursive(test_list, 3)
        False
    """

    start = time.time()
    a_list.sort()
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
            
    end = time.time()
    length = end - start
    return [length, found]


def rand_list(length):
    """Generates random list of numbers

    Args: length (int): Number of items in the list

    Ex: > rand_list(5)
        [4,1,3,2,5]
    """
    
    randlist = []
    for item in range(length):
        randlist.append(random.randint(1,length))
    return randlist


def main():
    """The main function of the program. Runs automatically"""

    tests = [500,1000,10000]
    for test in tests:
        counter = 100
        results = [0,0,0,0]
        while counter > 0:
            randlist = rand_list(test)
            results[0] += sequential_search(randlist, -1)[0]
            results[1] += ordered_sequential_search(randlist, -1)[0]
            results[2] += binary_search_iterative(randlist, -1)[0]
            results[3] += binary_search_recursive(randlist, -1)[0]
            counter -= 1
        print "For list of {}: ".format(test)
        print "Sequential Search took %10.7f seconds to run, on average" % \
              (results[0] / 100)
        print "Ordered Sequential Search " + \
                "took %10.7f seconds to run, on average" % \
              (results[1] / 100)
        print "Iterative Binary Search " + \
                "took %10.7f seconds to run, on average" % \
              (results[2] / 100)
        print "Recursive Binary Search " + \
                "took %10.7f seconds to run, on average" % \
              (results[3] / 100)

if __name__ == "__main__":
    main()
