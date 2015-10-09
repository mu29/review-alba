#-*- coding: utf-8 -*-

from Markov import *
from Crawler import *

crawler = Crawler()
markov = Markov()

reviews = crawler.get_pos_reviews(3000)
markov.make_database(reviews)

result = open('result.txt', 'w')

for i in range(0, 1000):
    comment = markov.make_comment()
    result.write(comment + '\n')
    print comment
