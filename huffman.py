import heapq
import os


class heap_node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right =None

    def __cmp__(self, other):
        if other is None:
            return -1
        if not isinstance(other, heap_node):
            return -1
        return self.frequency > other.frequency


class Compressing:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.code = {}
        self.remapping = {}

    def freq_dict(self,file):
        frequency = {}
        for char in file:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

