#-*- coding: utf-8 -*-

from Node import *

class Markov:
    def __init__(self):
        self.nodes = []

    def make_database(self, reviews):
        for review in reviews:
            words = review.split()
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
                    if words[i].find('.'): node.end = True
                    if words[i].find('!'): node.end = True
                    if words[i].find('?'): node.end = True
                    if words[i].find('.'): node.end = True
                    if words[i].find(u'ㅋ'): node.end = True

                    node.text = words[i]
                    if node.end: is_new_node = True
                    else: node.next = words[i + 1]

                    self.nodes.append(node)
                if is_new_node: node.start = True
