#!/usr/bin/python
# -*- coding: utf8 -*-

import random

images = [
            [
                "============",
                "=    oo    =",
                "=   o  o   =",
                "=  oooooo  =",
                "=  o    o  =",
                "=  o    o  =",
                "============"
            ],
            [
                "============",
                "=  ooooo   =",
                "=  o    o  =",
                "=  ooooo   =",
                "=  o    o  =",
                "=  ooooo   =",
                "============"
            ],
            [
                "============",
                "=   ooooo  =",
                "=  o       =",
                "=  o       =",
                "=  o       =",
                "=   ooooo  =",
                "============"
            ],
            [
                "============",
                "=  ooooo   =",
                "=  o    o  =",
                "=  o    o  =",
                "=  o    o  =",
                "=  ooooo   =",
                "============"
            ]
        ]


class Player:

    def __init__(self):
        self.steps = 0
        self.flipped = []

    def flipCell(self, cell):
        cell.flip()
        self.steps += 1
        self.flipped.append(cell)

    def flippedNewPair(self):
        return len(self.flipped) == 2

    def getPair(self):
        return (self.flipped.pop(), self.flipped.pop())

    def coverPair(self, cell_pair):
        for cell in cell_pair:
            cell.flip()

class Board(list):

    def __init__(self, cells):
        super(Board, self).__init__(cells)
        random.shuffle(self)   # miksuje elementy listy
        for i, cell in enumerate(self): cell.setIndex(i)

    def __str__(self):
        return "".join(["~" for line in range(38)])\
                +"\n"+"\n".join([line for line in self._getLines(0,3)])\
                +"\n"+"".join(["~" for line in range(38)])\
                +"\n"+"\n".join([line for line in self._getLines(3,6)])\
                +"\n"+"".join(["~" for line in range(38)])\
                +"\n"+"\n".join([line for line in self._getLines(6,8)])

    def _getLines(self, start, stop):
        iters = [iter(cell) for cell in self[start:stop]]
        while True:
            yield " ".join([next(itr) for itr in iters])

    def isCompleted(self):
        for cell in self:
            if cell.isCovered():
                return False
        return True

class Cell:

    image_covered = [
            "============",
            "============",
            "============",
            "============",
            "============",
            "============",
            "============"
        ]

    def __init__(self, image):
        self.image = image
        self.image_visible = self.image_covered

    def __iter__(self):
        return iter(self.image_visible)

    def __str__(self):
        return "\n".join(self.image_visible)

    def __eq__(self, other):
        return self.image== other.image

    def __ne__(self, other):
        return not self.__eq__(other)

    def setIndex(self, idx):
        self.image_covered = list(self.image_covered)
        self.flip(); self.flip()
#self.image_covered[3] = self.image_covered[3].format(idx)
        self.image_covered[3] = "=====("+str(idx)+")===="

    def flip(self):
        if self.image_visible == self.image_covered:
            self.image_visible = self.image
        else:
            self.image_visible = self.image_covered

    def isCovered(self):
        return self.image_visible == self.image_covered

###############################################################################
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cell_A = Cell(images[0])
cell_B = Cell(images[1])

player = Player()

board = Board([Cell(img) for img in images*2])


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def inputIsValid(str_input):
    return str_input.isdigit() and \
            int(str_input) < len(board) and \
            board[int(str_input)].isCovered()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

if __name__ == "__main__":
    while True:
        print board

        if board.isCompleted():
            print " > You win in: %d steps" % player.steps
            break

        if player.flippedNewPair():
            a, b = player.getPair()
            if a != b:
                player.coverPair([a, b])

        user_input = raw_input(" : ")

        if user_input == 'q':
            break

        if inputIsValid(user_input):
            idx = int(user_input)
            cell = board[idx]
            player.flipCell(cell)

        else:
            print " ! wrong input"

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
###############################################################################
