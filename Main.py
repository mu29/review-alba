#-*- coding: utf-8 -*-

from Markov import *
from Crawler import *

crawler = Crawler()
markov = Markov()

reviews = crawler.get_pos_reviews(1000)
markov.make_database(reviews)

for i in range(0, 100):
    print markov.make_comment()
