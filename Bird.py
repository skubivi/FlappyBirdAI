import random


class Bird:
    def __init__(self, w_n1=None, w_n2=None, w_n3=None):
        self.x = 80
        self.y = 240
        self.fit = 0
        self.death = False
        self.n1 = None
        self.w_n1 = w_n1
        self.n2 = None
        self.w_n2 = w_n2
        self.n3 = None
        self.w_n3 = w_n3
        self.t = 0
        self.output = None
