#!/usr/bin/python
# -*- coding: utf8 -*-

import random

board_visible = list("________")
board = ['A', 'B', 'C', 'D'] * 2
steps = 0

random.shuffle(board)   # miksuje elementy listy

flipped = []

while True:
    print " "+" ".join(board_visible)
    print " 0 1 2 3 4 5 6 7"

    if not '_' in board_visible:
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

    if user_input.isdigit():
        idx = int(user_input)
        if idx < len(board) and board_visible[idx] == "_":
            board_visible[idx] = board[idx]
            flipped.append(idx)
            steps += 1
            continue
    
    print " ! wrong input"
