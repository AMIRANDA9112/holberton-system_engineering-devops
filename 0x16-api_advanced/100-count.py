#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import sys

if __name__ == '__main__':
    words = __import__('100-count').words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:

        funct = [x for x in sys.argv[2].split()]

        result = words(sys.argv[1], funct)
