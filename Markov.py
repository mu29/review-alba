#-*- coding: utf-8 -*-

import random
from Node import *

class Markov:
    def __init__(self):
        self.data = open('data.txt', 'w')
        self.nodes = {}
        self.start_nodes = []

    def make_database(self, reviews):
        for review in reviews:
            review = review.encode('utf-8')
            self.data.write(review + '\n')
            words = review.split(' ')
            is_new_node = True
            for i in range(0, len(words) - 1):
                word = words[i]
                node = None
                if word in self.nodes:
                    node = self.nodes[word]
                    node.next.append(words[i + 1])
                else:
                    node = Node()
                    if i == len(words) - 1: node.end = True
                    if words[i].find('.') > 0: node.end = True
                    if words[i].find('!') > 0: node.end = True
                    if words[i].find('?') > 0: node.end = True
                    if words[i].find('.') > 0: node.end = True
                    if words[i].find('ㅋ') > 0: node.end = True

                    node.text = word
                    if node.end: is_new_node = True
                    else: node.next.append(words[i + 1])

                    self.nodes[word] = node
                if is_new_node and not node.end:
                    is_new_node = False
                    node.start = True
                    self.start_nodes.append(node)

            word = words[len(words) - 1]
            if not word in self.nodes:
                node = Node()
                node.text = word
                node.end = True
                self.nodes[word] = node


    def make_comment(self):
        index = random.randrange(0, len(self.start_nodes))
        start = self.start_nodes[index]

        return self.make_text(start.text, start)

    def make_text(self, text, node):
        if node.end == True:
            return text

        index = random.randrange(0, len(node.next))
        next_word = node.next[index]
        text += next_word + " "
        return self.make_text(text, self.nodes[next_word])
