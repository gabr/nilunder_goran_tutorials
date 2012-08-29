#!/usr/bin/python
# -*- coding: utf8 -*-

import random

class Cell:

    def __init__(self, char):

        self.char  = char
        self.image = '_'

    def __str__(self):

        return self.image

    def flip(self):

        if self.image == '_':
            self.image = self.char
        else:
            self.image = '_'

board_visible = list("________")
board = ['A', 'B', 'C', 'D'] * 2

steps = 0

random.shuffle(board)   # miksuje elementy listy

flipped = []

def printBoard(board):
    
    print " "+" ".join(board)
    print " 0 1 2 3 4 5 6 7"

def boardIsComplete(board):

    return (not '_' in board)

def inputIsValid(str_input):

    return str_input.isdigit() and \
            int(str_input) < len(board) and \
            board_visible[int(str_input)] == "_"

def flip(idx):
    
    if board_visible[idx] == '_':
        board_visible[idx] = board[idx]
        global steps
        steps += 1
        return

    board_visible[idx] = "_"

while True:

    printBoard(board_visible)

    if boardIsComplete(board_visible):
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
