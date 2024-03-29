#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.base_url = 'http://movie.naver.com/movie/point/af/list.nhn?target=after&page='

    def get_pos_reviews(self, pages):
        reviews = []
        for page in range(0, pages):
            reviews += self.get_reviews(page, True)

        return reviews

    def get_neg_reviews(self, pages):
        reviews = []
        for page in range(0, pages):
            reviews += self.get_reviews(page, False)

        return reviews

    def get_reviews(self, page, positive):
        document = urllib.urlopen(self.base_url + str(page))
        soup = BeautifulSoup(document, "html.parser")
        points = soup.find_all('td', attrs = { 'class' : 'point' })
        contents = soup.find_all('td', attrs = { 'class' : 'title' })

        reviews = []
        for i in range(0, len(points)):
            point = int(points[i].string)
            if ((positive and point > 8) or (not positive and point < 3)):
                text = contents[i].contents[3].contents[0].strip()
                text = text.encode('utf-8')
                reviews.append(text)

        return reviews
