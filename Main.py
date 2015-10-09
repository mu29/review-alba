#-*- coding: utf-8 -*-

from Markov import *
from Crawler import *

crawler = Crawler()
markov = Markov()

reviews = crawler.get_pos_reviews(100)
markov.make_database(reviews)

for i in range(0, 10):
    print markov.make_comment()
