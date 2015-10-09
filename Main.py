#-*- coding: utf-8 -*-

from Crawler import *

crawler = Crawler()
k = crawler.get_pos_reviews(1)
for i in range(0, len(k)):
    print k[i]
