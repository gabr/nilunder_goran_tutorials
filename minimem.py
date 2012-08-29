#!/usr/bin/python
# -*- coding: utf8 -*-

import random

class Board:

    def __init__(self, cells):

        self.cells = cells

    def __str__(self):

        return " ".join([str(c) for c in self.cells]) +\
                "\n0 1 2 3 4 5 6 7"

    def isCompleted(self):

        for cell in self.cells:
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

board = [Cell(c) for c in ['A', 'B', 'C', 'D'] * 2]

steps = 0

random.shuffle(board)   # miksuje elementy listy

flipped = []

def printBoard(board):
    
    print "",
    for cell in board:
        print cell,
    print "\n 0 1 2 3 4 5 6 7"


def inputIsValid(str_input):

    return str_input.isdigit() and \
            int(str_input) < len(board) and \
            board[int(str_input)].isCovered()

def flip(idx):
    
    global steps
    if board[idx].isCovered:
        steps += 1
    board[idx].flip()

if __name__ == "__main__":
    while True:

        printBoard(board)

        if boardIsComplete(board):
            print " > You win in: %d steps" % steps
            break

        if len(flipped) == 2:
            a, b = [board[i] for i in flipped]
            if a != b:
                for i in flipped: flip(i)
            flipped = []

        user_input = raw_input(" : ")

        if user_input == 'q':
            break

        if inputIsValid(user_input):

            idx = int(user_input)
            flip(idx)
            flipped.append(idx)
        else:
            print " ! wrong input"
