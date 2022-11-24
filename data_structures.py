from collections import deque
from heapq import heappop, heappush


class Queue:

    def __init__(self):
        self.__container = deque()

    @property
    def empty(self):
        return not self.__container

    def push(self, item):
        self.__container.append(item)

    def pop(self):
        return self.__container.popleft()

    def __repr__(self):
        return repr(self.__container)


class PriorityQueue:

    def __init__(self):
        self.__container = []

    @property
    def empty(self):
        return not self.__container

    def push(self, item):
        heappush(self.__container, item)

    def pop(self):
        return heappop(self.__container)

    def __repr__(self):
        return repr(self.__container)


class Stack:

    def __init__(self):
        self.__container = []

    @property
    def empty(self):
        if not self.__container:
            return True
        return False

    def pop(self):
        return self.__container.pop()

    def push(self, item):
        self.__container.append(item)

    def __repr__(self):
        return repr(self.__container)