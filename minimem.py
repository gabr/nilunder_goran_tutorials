#!/usr/bin/python
# -*- coding: utf8 -*-

import random

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

    def __str__(self):

        return " ".join([str(c) for c in self]) +\
                "\n0 1 2 3 4 5 6 7"

    def isCompleted(self):

        for cell in self:
            if cell.isCovered():
                return False
        return True

class Cell:

    def __init__(self, char):

        self.char  = char
        self.image = '_'

    def __str__(self):

        return self.image

    def __eq__(self, other):

        return self.image == other.image

    def __ne__(self, other):

        return not self.__eq__(other)

    def flip(self):

        if self.image == '_':
            self.image = self.char
        else:
            self.image = '_'

    def isCovered(self):

        return self.image == '_'

###############################################################################
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

player = Player()

board = Board([Cell(c) for c in ['A', 'B', 'C', 'D'] * 2])

random.shuffle(board)   # miksuje elementy listy

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
