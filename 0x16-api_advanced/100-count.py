#!/usr/bin/python3
""" Request recursively the top ten hot posts """

import requests


def count_words(subreddit, word_list, after=None, my_dict={}):
    """ API query subreddit """

    query = requests.get((
        'https://www.reddit.com/r/{}'
        '/hot.json'.format(subreddit)),
                         allow_redirects=False,
                         params={'after': after},
                         headers={'User-Agent': 'Pear'})

    if query and query.status_code == 200:
        list_query = query.json().get('data').get('children')
        for child in list_query:
            title1 = child.get('data').get('title')
            for word in word_list:
                try:
                    my_dict[word] += title1.lower().split().count(word.lower())
                except KeyError:
                    my_dict[word] = title1.lower().split().count(word.lower())

        after = query.json().get('data').get('after')

        if after is None:
            for key, val in sorted(my_dict.items(),
                                   key=lambda x: x[1], reverse=True):
                if val != 0:
                    print("{}: {}".format(key, val))
            return
        return count_words(subreddit, word_list, after, my_dict)
    else:
        return
