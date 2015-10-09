#-*- coding: utf-8 -*-

from Markov import *
from Crawler import *

crawler = Crawler()
k = crawler.get_pos_reviews(1)
markov = Markov()
markov.make_database(k)
