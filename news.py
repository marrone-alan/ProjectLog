#!/usr/bin/env python3
#
# A log consult to show info about articles, authors and requests.

import newsdb
# getTitles, getAuthors, getPercentage


def main():
    '''Call the methods from newsdb and show the results'''
    print('Question 1: What are the most popular three articles of all time?')
    for (title, views) in newsdb.getTitles():
        print("{} - {}".format(title, views))
    print('-----------------------------------------------------------------')
    print('Question 2: Who are the most popular article authors of all time?')
    for (name, views) in newsdb.getAuthors():
        print("{} - {}".format(name, views))
    print('-----------------------------------------------------------------')
    print('Question 3: Days when more than 1% of the requests have errors')
    for (day, error) in newsdb.getPercentage():
        print("{} - {}".format(day, error))
main()
