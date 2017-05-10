import os


def get_txt(filename):

    with open(filename, 'r') as f:
        reader =  f.next()
        print f.next()
        print reader


get_txt('test1.txt')