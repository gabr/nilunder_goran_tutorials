#!/usr/bin/python
# -*- coding: utf8 -*-

import random

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

def inputIsValid():

    return user_input.isdigit() and \
            int(user_input) < len(board) and \
            board_visible[int(user_input)] == "_"
while True:

    printBoard(board_visible)

    if boardIsComplete(board_visible):
        print " > You win in: %d steps" % steps
        break

    if len(flipped) == 2:
        a, b = [board[i] for i in flipped]
        if a != b:
            for i in flipped:
                board_visible[i] = "_"
        flipped = []

    user_input = raw_input(" : ")

    if user_input == 'q':
        break

    if inputIsValid():

        idx = int(user_input)
        board_visible[idx] = board[idx]
        flipped.append(idx)
        steps += 1
    else:
        print " ! wrong input"
